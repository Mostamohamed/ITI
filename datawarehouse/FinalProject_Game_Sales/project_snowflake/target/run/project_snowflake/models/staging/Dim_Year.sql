
  create or replace   view FINALPROJECT.RAW.Dim_Year
  
   as (
    SELECT 
    ROW_NUMBER() OVER (ORDER BY release_year) AS year_id,
    release_year
FROM FINALPROJECT.RAW.stg_databefore
WHERE release_year IS NOT NULL
GROUP BY release_year
  );

