import pandas as pd
from datetime import datetime
# import snowflake.connector
from dotenv import load_dotenv
import os
from tmdb_utils import get_media_from_2000
from process import process_data


load_dotenv()


# get data
movies_raw = get_media_from_2000("movie")
print(f"Got {len(movies_raw)} movies with revenue info.")

tv_raw = get_media_from_2000("tv")
print(f"Got {len(tv_raw)} TV shows")



# process and clean data
movies_dim, movies_date, movies_fact = process_data(movies_raw, "movie")
tv_dim, tv_date, tv_fact = process_data(tv_raw, "tv")

# concnate and drop duplicates if found
dim_title_df = pd.concat([movies_dim, tv_dim]).drop_duplicates()
dim_date_df =pd.concat([movies_date, tv_date])
fact_df = pd.concat([movies_fact, tv_fact])

# save to csv files
dim_title_df.to_csv('dim_title.csv', index=False) 
dim_date_df.to_csv('date.csv', index=False) 
fact_df.to_csv('fact.csv', index=False) 