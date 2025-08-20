SELECT 
    ROW_NUMBER() OVER (ORDER BY game_name) AS game_id,
    game_name
FROM {{ ref('stg_databefore') }}
GROUP BY game_name
