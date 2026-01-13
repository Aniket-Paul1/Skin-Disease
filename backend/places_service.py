import os
import requests

PLACES_KEY = os.getenv("GOOGLE_PLACES_API_KEY")


PLACES_NEARBY_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
PLACES_DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"


def fetch_dermatology_hospitals(lat, lng, radius=5000):
    params = {
        "location": f"{lat},{lng}",
        "radius": radius,
        "type": "hospital",
        "keyword": "dermatology",
        "key": PLACES_KEY
    }

    res = requests.get(PLACES_NEARBY_URL, params=params, timeout=10)
    res.raise_for_status()
    return res.json().get("results", [])


def fetch_place_details(place_id):
    params = {
        "place_id": place_id,
        "fields": "name,rating,opening_hours,geometry,formatted_address,url",
        "key": PLACES_KEY
    }

    res = requests.get(PLACES_DETAILS_URL, params=params, timeout=10)
    res.raise_for_status()
    return res.json().get("result", {})
