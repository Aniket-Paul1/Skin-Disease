import os
import sys
import tempfile
import requests
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from geopy.distance import geodesic
from backend.places_service import (
    fetch_dermatology_hospitals,
    fetch_place_details,
    PLACES_KEY
)
from backend.location_data import STATE_CITY_MAP

print("MAIN USING GOOGLE PLACES KEY:", PLACES_KEY[:6], "****")

# --------------------------------------------------
# PATH SETUP (reuse your existing ml_code)
# --------------------------------------------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from ml_code.ensemble.predict import predict_image

# --------------------------------------------------
# APP INIT
# --------------------------------------------------
app = FastAPI(title="AI Skin Disease Detection API")

# --------------------------------------------------
# CORS (React frontend support)
# --------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development; restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

# --------------------------------------------------
# PREDICTION ENDPOINT
# --------------------------------------------------
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Validate image using PIL (safer than content_type)
        image = Image.open(file.file).convert("RGB")

        # Save image temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            image.save(tmp.name)
            img_path = tmp.name

        # Run your existing ML pipeline
        result = predict_image(img_path)

    except HTTPException:
        raise

    except Exception as e:
        print("BACKEND ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if "img_path" in locals() and os.path.exists(img_path):
            os.remove(img_path)

    return {
        "disease": result["final_label"],
        "confidence": round(
            result["confidence"] * 100 if result["source"] == "cnn"
            else result["confidence"] * 1000,
            2
        ),
        "source": result["source"],
        "description": result.get("reason", "")
    }


# ------------------------------
# Overpass fallback servers
# ------------------------------
OVERPASS_SERVERS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass.nchc.org.tw/api/interpreter",
]

# ------------------------------
# Helper: robust Overpass runner
# ------------------------------
def run_overpass(query: str, headers: dict):
    for url in OVERPASS_SERVERS:
        try:
            res = requests.post(
                url,
                data=query,
                headers=headers,
                timeout=25
            )
            if res.status_code == 200 and res.text.strip():
                return res.json()
            else:
                print(f"Overpass failed at {url}: {res.status_code}")
        except Exception as e:
            print(f"Overpass exception at {url}: {e}")
    return None

def geocode_city_state(city: str, state: str):
    headers = {
        "User-Agent": "AI-Skin-Disease-App/1.0 (academic-project)"
    }

    res = requests.get(
        "https://nominatim.openstreetmap.org/search",
        params={
            "q": f"{city}, {state}, India",
            "format": "json",
            "limit": 1
        },
        headers=headers,
        timeout=10
    )

    if res.status_code != 200:
        raise RuntimeError("Geocoding failed: HTTP error")

    data = res.json()
    if not data:
        raise RuntimeError("Geocoding failed: No results")

    lat = float(data[0]["lat"])
    lng = float(data[0]["lon"])

    return lat, lng




# ==================================================
#  NEARBY DERMATOLOGISTS / HOSPITALS (FINAL)
# ==================================================
@app.get("/nearby-dermatologists")
def find_nearby_dermatologists(
    city: str,
    state: str,
    radius_km: int = 20
):
    headers = {
        "User-Agent": "AI-Skin-Disease-App/1.0 (academic-project)"
    }

    # ---------- 1️⃣ GEOCODING ----------
    try:
        geo_res = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={
                "q": f"{city}, {state}, India",
                "format": "json",
                "limit": 1
            },
            headers=headers,
            timeout=10
        )

        if geo_res.status_code != 200 or not geo_res.text.strip():
            return []

        geo = geo_res.json()
        if not geo:
            return []

        lat, lon = float(geo[0]["lat"]), float(geo[0]["lon"])

    except Exception as e:
        print("Geocoding failed:", e)
        return []

    # ---------- 2️⃣ OVERPASS QUERY (DISEASE-AGNOSTIC) ----------
    query = f"""
    [out:json][timeout:25];
    (
      node["amenity"="hospital"](around:{radius_km*1000},{lat},{lon});
      node["amenity"="clinic"](around:{radius_km*1000},{lat},{lon});
      node["healthcare"="hospital"](around:{radius_km*1000},{lat},{lon});
      node["healthcare"="clinic"](around:{radius_km*1000},{lat},{lon});
      node["healthcare:speciality"~"dermatology",i](around:{radius_km*1000},{lat},{lon});
      way["amenity"="hospital"](around:{radius_km*1000},{lat},{lon});
      way["amenity"="clinic"](around:{radius_km*1000},{lat},{lon});
    );
    out center tags;
    """

    data = run_overpass(query, headers)
    if not data:
        return []

    # ---------- 3️⃣ PARSE RESULTS ----------
    results = []

    for el in data.get("elements", []):
        dlat = el.get("lat") or el.get("center", {}).get("lat")
        dlon = el.get("lon") or el.get("center", {}).get("lon")

        if not dlat or not dlon:
            continue

        tags = el.get("tags", {})
        distance = round(
            geodesic((lat, lon), (dlat, dlon)).km, 2
        )

        results.append({
            "name": tags.get("name", "Hospital / Clinic"),
            "distance_km": distance,
            "type": (
                "Dermatology Department"
                if "derma" in str(tags.get("healthcare:speciality", "")).lower()
                else "Hospital / Clinic"
            ),
            "address": (
                tags.get("addr:full")
                or tags.get("addr:street")
                or tags.get("addr:city")
                or "Address not available"
            ),
            "maps_url": f"https://www.google.com/maps?q={dlat},{dlon}"
        })

    results.sort(key=lambda x: x["distance_km"])
    return results[:10]

from typing import Optional

@app.get("/verified-doctors")
def get_verified_doctors(
    city: Optional[str] = None,
    state: Optional[str] = None,
    lat: Optional[float] = None,
    lng: Optional[float] = None
):
    try:
        if lat is not None and lng is not None:
            # 📍 GPS-based search
            hospitals = fetch_dermatology_hospitals(lat, lng)

        elif city and state:
            city = city.strip().title()
            state = state.strip().title()
            lat, lng = geocode_city_state(city, state)
            hospitals = fetch_dermatology_hospitals(lat, lng)

        else:
            return []

        hospitals_sorted = sorted(
            hospitals,
            key=lambda h: h["rating"] if isinstance(h.get("rating"), (int, float)) else 0,
            reverse=True
        )

        return hospitals_sorted

    except Exception as e:
        print("Verified doctors error:", e)
        return []



@app.get("/locations/states")
def get_states():
    return sorted(STATE_CITY_MAP.keys())

@app.get("/locations/cities")
def get_cities(state: str):
    cities = STATE_CITY_MAP.get(state)
    if not cities:
        return []
    return cities
