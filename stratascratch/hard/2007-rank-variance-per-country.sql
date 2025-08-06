/*
2019 Decemeber table and 2020 december table ranked

take a difference where rank_diff is negative
*/

WITH ranked_2019 AS (
    SELECT country, 
        DENSE_RANK() OVER (ORDER BY sum(number_of_comments) DESC) AS rnk
    FROM fb_comments_count JOIN fb_active_users USING(user_id)  
    WHERE EXTRACT(MONTH FROM created_at) = 12 
        AND EXTRACT(YEAR FROM created_at) = 2019 
    GROUP BY country
), ranked_2020 AS (
    SELECT country, 
        DENSE_RANK() OVER (ORDER BY sum(number_of_comments) DESC) AS rnk
    FROM fb_comments_count JOIN fb_active_users USING(user_id)  
    WHERE EXTRACT(MONTH FROM created_at) = 1
        AND EXTRACT(YEAR FROM created_at) = 2020 
    GROUP BY country
)

SELECT country FROM ranked_2019 r19 JOIN ranked_2020 r20 USING(country) WHERE r20.rnk-r19.rnk < 0
