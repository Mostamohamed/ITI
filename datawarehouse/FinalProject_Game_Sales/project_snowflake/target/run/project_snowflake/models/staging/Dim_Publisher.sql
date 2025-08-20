
  create or replace   view FINALPROJECT.RAW.Dim_Publisher
  
   as (
    SELECT 
    ROW_NUMBER() OVER (ORDER BY publisher_name) AS publisher_id,
    publisher_name
FROM FINALPROJECT.RAW.stg_databefore
GROUP BY publisher_name
  );

