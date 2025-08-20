SELECT 
    ROW_NUMBER() OVER (ORDER BY platform_name) AS platform_id,
    platform_name
FROM FINALPROJECT.RAW.stg_databefore
GROUP BY platform_name