
  create or replace   view FINANCE_DB.RAW.my_second_dbt_model
  
  
  
  
  as (
    -- Use the `ref` function to select from other models

select *
from FINANCE_DB.RAW.my_first_dbt_model
where id = 1
  );

