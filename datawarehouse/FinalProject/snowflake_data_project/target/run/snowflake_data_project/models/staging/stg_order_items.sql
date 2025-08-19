
  create or replace   view FINANCE_DB.RAW.stg_order_items
  
   as (
    SELECT
id AS item_id,
order_id,
product_id,
quantity,
unit_price, 
(quantity * unit_price) AS total_price 
FROM finance_db.raw.order_items
  );

