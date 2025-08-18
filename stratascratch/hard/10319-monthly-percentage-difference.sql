/* Sum up by month
then we take the lag and 
then calculate the percentage

*/
WITH monthly_revenue AS (
    SELECT to_char(created_at, 'YYYY-MM') as year_month, SUM(value) AS revenue
    FROM sf_transactions
    GROUP BY to_char(created_at,'YYYY-MM')
),
month_by_month_revenue AS (
    SELECT year_month, revenue, LAG(revenue, 1, 0) OVER (ORDER BY year_month ASC) AS last_month_rev
    FROM monthly_revenue
)

SELECT year_month, (CASE WHEN NOT last_month_rev = 0 THEN round(((revenue-last_month_rev)/last_month_rev) * 100, 2) ELSE NULL END)
FROM month_by_month_revenue
