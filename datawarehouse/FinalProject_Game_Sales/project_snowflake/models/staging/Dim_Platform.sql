SELECT 
    ROW_NUMBER() OVER (ORDER BY platform_name) AS platform_id,
    platform_name
FROM {{ ref('stg_databefore') }}
GROUP BY platform_name
