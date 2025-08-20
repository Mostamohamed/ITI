
  create or replace   view FINALPROJECT.RAW.Dim_Genre
  
   as (
    SELECT 
    ROW_NUMBER() OVER (ORDER BY genre_name) AS genre_id,
    genre_name
FROM FINALPROJECT.RAW.stg_databefore
GROUP BY genre_name
  );

