import os
import requests
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(ENV_PATH)

PLACES_KEY = os.getenv("GOOGLE_PLACES_API_KEY")

print("USING GOOGLE PLACES KEY:", PLACES_KEY[:6] if PLACES_KEY else "NOT FOUND")

if not PLACES_KEY:
    raise RuntimeError("GOOGLE_PLACES_API_KEY not loaded")


PLACES_NEARBY_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
PLACES_DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"


def fetch_dermatology_hospitals(lat, lng, radius=7000):
    if not PLACES_KEY:
        raise RuntimeError("GOOGLE_PLACES_API_KEY not loaded")

    print("USING GOOGLE PLACES KEY:", PLACES_KEY[:6], "****")
    print("SEARCHING NEAR:", lat, lng)

    # Broad but safe keywords
    keywords = [
        "dermatology",
        "skin clinic",
        "skin hospital",
        "dermatologist",
        "chर्म रोग",          # Hindi (important for India)
        "skin care clinic",
        "cosmetic clinic"
    ]

    collected = {}

    for keyword in keywords:
        params = {
            "location": f"{lat},{lng}",
            "radius": radius,
            "type": "hospital",
            "keyword": keyword,
            "key": PLACES_KEY
        }

        res = requests.get(PLACES_NEARBY_URL, params=params, timeout=10)
        res.raise_for_status()
        data = res.json()

        for place in data.get("results", []):
            place_id = place.get("place_id")
            if not place_id:
                continue

            # Deduplicate across keyword searches
            collected[place_id] = place

    results = []

    for place in collected.values():
        name = place.get("name", "").lower()
        types = place.get("types", [])

        # 🔒 FINAL dermatology filter (important)
        if not any(
            k in name
            for k in ["derma", "skin", "cosmetic", "चर्म"]
        ):
            continue

        results.append({
            "name": place.get("name"),
            "address": place.get("vicinity"),
            "rating": place.get("rating"),
            "open_now": place.get("opening_hours", {}).get("open_now"),
            "location": {
                "lat": place["geometry"]["location"]["lat"],
                "lng": place["geometry"]["location"]["lng"],
            },
            "map_url": f"https://www.google.com/maps/place/?q=place_id:{place.get('place_id')}"
        })

    # ⭐ Sort by real Google rating
    results.sort(
        key=lambda x: x.get("rating", 0) or 0,
        reverse=True
    )

    print("DERMATOLOGY RESULTS FOUND:", len(results))
    return results




def fetch_place_details(place_id):
    params = {
        "place_id": place_id,
        "fields": "name,rating,opening_hours,geometry,formatted_address,url",
        "key": PLACES_KEY
    }

    res = requests.get(PLACES_DETAILS_URL, params=params, timeout=10)
    res.raise_for_status()
    return res.json().get("result", {})
