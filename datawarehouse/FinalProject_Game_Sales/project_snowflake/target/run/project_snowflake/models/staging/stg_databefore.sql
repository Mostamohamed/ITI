
  create or replace   view FINALPROJECT.RAW.stg_databefore
  
   as (
    WITH cleaned AS (
    SELECT
        CAST(Rank AS INT) AS raw_rank_id,
        Name AS game_name,
        Platform AS platform_name,
        TRY_CAST(Year AS INT) AS release_year,
        Genre AS genre_name,
        Publisher AS publisher_name,

        -- Since columns are DECIMAL, handle NULL values directly
        na_sales AS na_sales_raw,
        eu_sales AS eu_sales_raw,
        jp_sales AS jp_sales_raw,
        other_sales AS other_sales_raw,
        global_sales AS global_sales_raw
    FROM FINALPROJECT.RAW.DATABEFORE
    WHERE Name IS NOT NULL
      AND Platform IS NOT NULL
      AND Year IS NOT NULL
      AND Genre IS NOT NULL
      AND Publisher IS NOT NULL
      AND na_sales IS NOT NULL
      AND eu_sales IS NOT NULL
      AND jp_sales IS NOT NULL
      AND other_sales IS NOT NULL
      AND global_sales IS NOT NULL
)

SELECT
    raw_rank_id,
    game_name,
    platform_name,
    release_year,
    genre_name,
    publisher_name,

    -- Convert DECIMAL to FLOAT and handle any remaining NULLs
    COALESCE(CAST(na_sales_raw AS FLOAT), 0.0)    AS north_america_sales_million,
    COALESCE(CAST(eu_sales_raw AS FLOAT), 0.0)    AS europe_sales_million,
    COALESCE(CAST(jp_sales_raw AS FLOAT), 0.0)    AS japan_sales_million,
    COALESCE(CAST(other_sales_raw AS FLOAT), 0.0) AS other_region_sales_million,
    COALESCE(CAST(global_sales_raw AS FLOAT), 0.0) AS global_sales_million
FROM cleaned
  );

