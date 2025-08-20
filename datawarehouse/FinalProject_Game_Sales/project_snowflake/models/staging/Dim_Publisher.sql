SELECT 
    ROW_NUMBER() OVER (ORDER BY publisher_name) AS publisher_id,
    publisher_name
FROM {{ ref('stg_databefore') }}
GROUP BY publisher_name