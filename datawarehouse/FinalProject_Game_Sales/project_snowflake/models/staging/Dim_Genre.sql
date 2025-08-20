SELECT 
    ROW_NUMBER() OVER (ORDER BY genre_name) AS genre_id,
    genre_name
FROM {{ ref('stg_databefore') }}
GROUP BY genre_name
