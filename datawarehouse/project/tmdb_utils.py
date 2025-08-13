import requests
import os
import time
from dotenv import load_dotenv
from datetime import date

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

def get_details(media_type, media_id):
    """Fetch details for a single movie or TV show to get revenue."""
    url = f"{BASE_URL}/{media_type}/{media_id}"
    params = {"api_key": API_KEY, "language": "en-US"}
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json()

def get_media_from_2000(media_type):
    """Fetch movies or TV shows from 2000 and get their revenue."""
    if media_type == "movie":
        date_gte = "primary_release_date.gte"
        date_lte = "primary_release_date.lte"
    elif media_type == "tv":
        date_gte = "first_air_date.gte"
        date_lte = "first_air_date.lte"
    else:
        raise ValueError("media_type must be 'movie' or 'tv'")

    url = f"{BASE_URL}/discover/{media_type}"
    today = date.today().strftime("%Y-%m-%d")

    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "sort_by": "popularity.desc",
        date_gte: "1950-01-01",
        date_lte: today,
        "page": 1
    }

    all_results = []
    for page in range(1, 30):  # limit pages to avoid hitting rate limits
        params["page"] = page
        r = requests.get(url, params=params)
        r.raise_for_status()
        data = r.json()
        results = data.get("results", [])
        
        for item in results:
            details = get_details(media_type, item["id"])
            item["revenue"] = details.get("revenue", None)
            all_results.append(item)

    return all_results
