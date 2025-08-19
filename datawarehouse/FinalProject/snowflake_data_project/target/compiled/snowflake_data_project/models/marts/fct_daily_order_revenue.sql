select
o.order_date, 
O.order_id,
sum(total_price) AS total_price 
from 
FINANCE_DB.RAW.stg_orders O 
LEFT JOIN FINANCE_DB.RAW.stg_order_items OI
ON O.ORDER_ID=OI.ORDER_ID
GROUP BY 1,2