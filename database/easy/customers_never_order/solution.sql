-- Write your PostgreSQL query statement below
WITH customer_orders AS (
    SELECT 
    C.name AS customer_name, 
    O.id AS order_id
    FROM Customers C
    LEFT JOIN Orders O
        ON C.id = O.customerId
)
SELECT 
    customer_name AS "Customers"
FROM customer_orders 
WHERE 
    order_id IS NULL