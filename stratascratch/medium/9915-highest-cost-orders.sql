/*
Finds the customers with the highest daily total cost order 2019-02-01 and 2019-05-01.

We do this using a correlated subquery that finds for each date the customer with the highest total cost 
*/
SELECT first_name, order_date, sum(total_order_cost) 
FROM customers c JOIN orders o ON c.id = o.cust_id
WHERE order_date BETWEEN '2019-02-01' AND '2019-05-01'
GROUP BY order_date, c.first_name 
HAVING sum(total_order_cost) >= (
    SELECT sum(o2.total_order_cost) 
    FROM customers c2 JOIN orders o2 ON c2.id = o2.cust_id 
    WHERE o2.order_date = o.order_date 
    GROUP BY o2.order_date, c2.first_name 
    ORDER BY sum(o2.total_order_cost) DESC LIMIT 1
)
ORDER BY order_date ASC, sum(total_order_cost) DESC

