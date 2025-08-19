
  create or replace   view FINANCE_DB.RAW.stg_products
  
   as (
    SELECT
id AS product_id,
name AS product_name,
category AS product_category,
price AS product_price
FROM finance_db.raw.products
  );

