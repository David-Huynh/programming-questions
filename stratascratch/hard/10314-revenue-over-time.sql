/*
Calculates the net revenue per month and then computes a 3 month rolling average/moving average
*/
WITH month_avg AS (
    SELECT to_char(created_at, 'YYYY-MM') AS date, SUM(purchase_amt) AS m_total
    FROM amazon_purchases 
    WHERE purchase_amt>=0 
    GROUP BY to_char(created_at, 'YYYY-MM') 
    ORDER BY to_char(created_at, 'YYYY-MM') ASC
)
SELECT 
    date,
    AVG(m_total) 
    OVER(
        ORDER BY date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) 
FROM month_avg 
