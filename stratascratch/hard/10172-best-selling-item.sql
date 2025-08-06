/* 
Window function to get the sum of the total paid per item per month then rank it
*/
WITH all_totals AS (
    SELECT EXTRACT(MONTH FROM invoicedate) AS month, 
        description, 
        sum(unitprice*quantity) AS total_paid, 
        rank() OVER(
            PARTITION BY EXTRACT(MONTH FROM invoicedate)
            ORDER BY sum(unitprice * quantity) DESC
        ) AS rnk 
        FROM online_retail GROUP BY description,month)
SELECT month, description, total_paid FROM all_totals WHERE rnk = 1

