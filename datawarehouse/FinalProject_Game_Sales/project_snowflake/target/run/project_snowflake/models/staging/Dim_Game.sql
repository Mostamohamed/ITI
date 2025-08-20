
  create or replace   view FINALPROJECT.RAW.Dim_Game
  
   as (
    SELECT 
    ROW_NUMBER() OVER (ORDER BY game_name) AS game_id,
    game_name
FROM FINALPROJECT.RAW.stg_databefore
GROUP BY game_name
  );

