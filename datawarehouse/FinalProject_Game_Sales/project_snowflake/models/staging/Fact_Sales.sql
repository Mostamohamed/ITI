SELECT
    ROW_NUMBER() OVER (ORDER BY g.game_name, p.platform_name, y.release_year) AS sales_id,

    -- foreign keys from dimensions
    g.game_id,
    p.platform_id,
    y.year_id,
    ge.genre_id,
    pub.publisher_id,

    -- measures
    s.north_america_sales_million,
    s.europe_sales_million,
    s.japan_sales_million,
    s.other_region_sales_million,
    s.global_sales_million
FROM {{ ref('stg_databefore') }} s
JOIN {{ ref('Dim_Game') }} g 
    ON s.game_name = g.game_name
JOIN {{ ref('Dim_Platform') }} p 
    ON s.platform_name = p.platform_name
LEFT JOIN {{ ref('Dim_Year') }} y  
    ON s.release_year = y.release_year
JOIN {{ ref('Dim_Genre') }} ge     
    ON s.genre_name = ge.genre_name
JOIN {{ ref('Dim_Publisher') }} pub 
    ON s.publisher_name = pub.publisher_name
