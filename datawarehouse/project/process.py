import pandas as pd
from datetime import datetime
from genre_mapping import MOVIE_GENRES, TV_GENRES
import numpy as np

def process_data(raw_data, media_type):
    # Choose genre map and release column
    if media_type == "movie":
        genre_map = MOVIE_GENRES
        release_col = "release_date"
        title_col = "title"
    else:
        genre_map = TV_GENRES
        release_col = "first_air_date"
        title_col = "name"

    # Create DataFrame
    df = pd.DataFrame(raw_data)

    # Parse release date components
    df["release_date_parsed"] = pd.to_datetime(df[release_col], errors="coerce")
    df["release_year"] = df["release_date_parsed"].dt.year
    df["release_month"] = df["release_date_parsed"].dt.month
    df["release_day"] = df["release_date_parsed"].dt.day
    df["release_quarter"] = df["release_date_parsed"].dt.quarter
    df["release_weekday"] = df["release_date_parsed"].dt.day_name()

    # Map genre IDs to names
    df["genre"] = df["genre_ids"].apply(
        lambda ids: ", ".join([genre_map.get(i, "Unknown") for i in ids])
    )

    # Common fields
    df["content_type"] = media_type
    df["title_id"] = df["id"]
    df["title_name"] = df[title_col].str.strip()

    if "revenue" not in df.columns:
        df["revenue"] = None

    # =====================
    # Dimension: Title
    # =====================
    dim_title = df[
        ["title_id", "title_name", "genre", "content_type", "original_language"]
    ].drop_duplicates()

    # =====================
    # Dimension: Date
    # =====================
    dim_date = df[
        ["release_date_parsed", "release_year", "release_month", "release_day",
         "release_quarter", "release_weekday"]
    ].drop_duplicates().reset_index(drop=True)

    # Generate unique date_key (numeric + random)
    dim_date["date_key"] = dim_date["release_date_parsed"].dt.strftime("%Y%m%d") + \
                           "_" + np.random.randint(1000, 9999, size=len(dim_date)).astype(str)

    dim_date = dim_date[
        ["date_key", "release_date_parsed", "release_year", "release_month",
         "release_day", "release_quarter", "release_weekday"]
    ]

    # Merge date_key back to main df
    df = df.merge(dim_date[["release_date_parsed", "date_key"]], on="release_date_parsed", how="left")

    # =====================
    # Fact table
    # =====================
    fact = df[["title_id", "date_key", "popularity", "vote_average", "vote_count", "revenue"]]
    fact["rank"] = fact["popularity"].rank(ascending=False).astype(int)

    return dim_title, dim_date, fact
