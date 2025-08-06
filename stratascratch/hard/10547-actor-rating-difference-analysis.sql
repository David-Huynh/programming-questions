/*
The hardest part is find the latest rating and realizing that you can calculate the average by summing then dividing by count.
The CTE actor_latest_rating finds actors with the rating of their latest film.

We then use total_rating to find the sum and count of all rating for each actor.
Finally, we calculate the average rating and the difference between the latest rating and the average of previous ratings. 
*/

WITH actor_latest_rating AS (
SELECT actor_name, film_rating AS latest_rating
FROM actor_rating_shift a1 
WHERE a1.release_date=(
    SELECT MAX(release_date)
    FROM actor_rating_shift a2 
    WHERE a1.actor_name=a2.actor_name
) 
), total_rating AS (SELECT actor_name, SUM(film_rating) AS total, COUNT(*) AS film_count FROM actor_rating_shift GROUP BY actor_name)

SELECT 
    actor_name, 
    (CASE WHEN film_count=1 THEN total WHEN film_count > 1 THEN ((total-latest_rating)/(film_count-1)) ELSE 0 END)as avg_rating, 
    latest_rating, 
    (CASE WHEN film_count > 1 THEN round((latest_rating-((total-latest_rating)/(film_count-1)))::numeric,2) ELSE 0 END) AS rating_difference 
FROM actor_latest_rating JOIN total_rating USING(actor_name) 
ORDER BY actor_name
