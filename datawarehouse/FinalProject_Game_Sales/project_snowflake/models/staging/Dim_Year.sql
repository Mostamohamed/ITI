SELECT 
    ROW_NUMBER() OVER (ORDER BY release_year) AS year_id,
    release_year
FROM {{ ref('stg_databefore') }}
WHERE release_year IS NOT NULL
GROUP BY release_year
