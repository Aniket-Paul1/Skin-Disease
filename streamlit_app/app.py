import sys
import os
import tempfile
import sqlite3
import requests
import streamlit as st
from PIL import Image
from geopy.distance import geodesic
import pandas as pd

# --------------------------------------------------
# PATH SETUP
# --------------------------------------------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from ml_code.ensemble.predict import predict_image
from db import (
    init_db,
    register_user,
    authenticate_user,
    save_prediction,
    get_user_predictions
)

DB_PATH = os.path.join(os.path.dirname(__file__), "predictions.db")

# --------------------------------------------------
# INIT
# --------------------------------------------------
init_db()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --------------------------------------------------
# CONSTANTS
# --------------------------------------------------
INDIAN_STATES = [
    "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh",
    "Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand",
    "Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur",
    "Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan",
    "Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh",
    "Uttarakhand","West Bengal",
    "Andaman and Nicobar Islands","Chandigarh",
    "Dadra and Nagar Haveli and Daman and Diu","Delhi",
    "Jammu and Kashmir","Ladakh","Lakshadweep","Puducherry"
]

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AI-Based Skin Disease Detection System",
    page_icon="🩺",
    layout="wide"
)

# --------------------------------------------------
# AUTH UI
# --------------------------------------------------
def show_register():
    st.subheader("📝 Register")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    state = st.selectbox("State", INDIAN_STATES)
    city = st.text_input("City")

    if st.button("Create Account"):
        if not username or not email or not password or not city:
            st.error("All fields are required")
            return

        ok, msg = register_user(username, email, password, city, state)
        if ok:
            st.success("Registered successfully. Please login.")
        else:
            st.error(msg)


def show_login():
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = authenticate_user(username, password)
        if user:
            st.session_state.logged_in = True
            st.session_state.user_id = user["id"]
            st.session_state.username = user["username"]
            st.session_state.city = user["city"]
            st.session_state.state = user["state"]
            st.rerun()
        else:
            st.error("Invalid username or password")

# --------------------------------------------------
# ACCESS CONTROL
# --------------------------------------------------
st.title("AI-Based Skin Disease Detection System")

if not st.session_state.logged_in:
    choice = st.radio("Select", ["Login", "Register"])

    if choice == "Login":
        show_login()
    else:
        show_register()

    st.stop()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:
    st.write(f"👤 {st.session_state.username}")
    st.write(f"📍 {st.session_state.city}, {st.session_state.state}")
    if st.button("Logout"):
        st.session_state.clear()
        st.rerun()

st.warning("⚠ Academic & research use only. Not a medical diagnosis tool.")

# --------------------------------------------------
# DOCTOR SEARCH (LOCATION-ONLY, CACHED)
# --------------------------------------------------
@st.cache_data(show_spinner=False)
def find_nearby_doctors(city, state, radius_km=25):
    headers = {"User-Agent": "AI-Skin-App/1.0"}

    # Geocode
    try:
        geo = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={"q": f"{city}, {state}, India", "format": "json", "limit": 1},
            headers=headers,
            timeout=10
        ).json()

        if not geo:
            return []

        city_lat = float(geo[0]["lat"])
        city_lon = float(geo[0]["lon"])
    except Exception:
        return []

    # Broad Overpass query (intentionally disease-agnostic)
    query = f"""
    [out:json];
    (
      node["amenity"="doctors"](around:{radius_km*1000},{city_lat},{city_lon});
      node["healthcare"="doctor"](around:{radius_km*1000},{city_lat},{city_lon});
      node["amenity"="clinic"](around:{radius_km*1000},{city_lat},{city_lon});
      node["healthcare"="clinic"](around:{radius_km*1000},{city_lat},{city_lon});
      node["amenity"="hospital"](around:{radius_km*1000},{city_lat},{city_lon});
      way["amenity"="clinic"](around:{radius_km*1000},{city_lat},{city_lon});
      way["amenity"="hospital"](around:{radius_km*1000},{city_lat},{city_lon});
    );
    out center tags;
    """

    try:
        res = requests.post(
            "https://overpass-api.de/api/interpreter",
            data=query,
            headers=headers,
            timeout=30
        )
        if res.status_code != 200:
            return []
        data = res.json()
    except Exception:
        return []

    doctors = []
    for el in data.get("elements", []):
        lat = el.get("lat") or el.get("center", {}).get("lat")
        lon = el.get("lon") or el.get("center", {}).get("lon")
        if not lat or not lon:
            continue

        name = el.get("tags", {}).get("name", "Clinic / Hospital")
        distance = round(
            geodesic((city_lat, city_lon), (lat, lon)).km, 2
        )

        doctors.append({
            "name": name,
            "distance": distance,
            "maps": f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
        })

    doctors.sort(key=lambda x: x["distance"])
    return doctors[:10]

# --------------------------------------------------
# TABS
# --------------------------------------------------
tab_predict, tab_history, tab_profile, tab_admin = st.tabs(
    ["🧠 Predict", "📜 History", "👤 Profile", "🛠 Admin"]
)

# ================= PREDICT =================
with tab_predict:
    uploaded = st.file_uploader("Upload skin image", ["jpg", "jpeg", "png", "webp"])

    if uploaded:
        img = Image.open(uploaded).convert("RGB")
        st.image(img, use_container_width=True)

        if st.button("Analyze Image"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
                img.save(tmp.name)
                result = predict_image(tmp.name)

            label = result["final_label"]
            conf = result["confidence"]
            src = result["source"]

            conf = conf * 100 if src == "cnn" else conf * 1000
            conf = round(min(conf, 99.99), 2)

            st.success(f"Disease: {label}")
            st.info(f"Confidence: {conf}%")

            st.subheader("📍 Nearest Dermatologists")
            doctors = find_nearby_doctors(
                st.session_state.city,
                st.session_state.state
            )

            if doctors:
                for d in doctors:
                    st.markdown(f"**{d['name']}** ({d['distance']} km)")
                    st.markdown(f"[Open in Google Maps]({d['maps']})")
            else:
                st.warning("Nearby clinics could not be fetched at the moment.")

            save_prediction(
                st.session_state.user_id,
                label,
                conf,
                src
            )

# ================= HISTORY =================
with tab_history:
    history = get_user_predictions(st.session_state.user_id)
    if not history:
        st.info("No prediction history.")
    else:
        for i, (d, c, s, t) in enumerate(history, 1):
            with st.expander(f"{i}. {d} — {t.split('T')[0]}"):
                st.write(f"Confidence: {c}%")
                st.write(f"Source: {s.upper()}")

# ================= PROFILE =================
with tab_profile:
    st.subheader("Update Profile")

    state = st.selectbox(
        "State",
        INDIAN_STATES,
        index=INDIAN_STATES.index(st.session_state.state)
    )
    city = st.text_input("City", st.session_state.city)

    if st.button("Save Profile"):
        if not city:
            st.error("City cannot be empty")
        else:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute(
                "UPDATE users SET city=?, state=? WHERE id=?",
                (city, state, st.session_state.user_id)
            )
            conn.commit()
            conn.close()

            st.session_state.city = city
            st.session_state.state = state
            st.success("Profile updated successfully")

# ================= ADMIN =================
with tab_admin:
    if st.session_state.username != "admin":
        st.warning("Admin access only.")
    else:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute("SELECT COUNT(*) FROM users")
        st.metric("Total Users", cur.fetchone()[0])

        cur.execute("SELECT COUNT(*) FROM predictions")
        st.metric("Total Predictions", cur.fetchone()[0])

        conn.close()

st.caption("AI Skin Disease Detection System | Academic Project")
