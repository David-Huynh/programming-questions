/*
For each actor ranks their best genres first 

Then for each actors best genre ranks the actor that receives the best average ratings

Then gets the Top 3 best rated actors in their best genre
*/
WITH actor_genre_rank AS (
    SELECT actor_name, genre, avg(movie_rating) AS avg_rating, DENSE_RANK() OVER (PARTITION BY actor_name ORDER BY count(*) DESC, avg(movie_rating) DESC) AS rnk
    FROM top_actors_rating
    GROUP BY actor_name, genre
), top_actors_by_genre AS (
    SELECT actor_name, genre, avg_rating, DENSE_RANK() OVER(ORDER BY avg_rating DESC) AS rank 
    FROM actor_genre_rank
    WHERE rnk = 1
    ORDER BY avg_rating DESC,actor_name DESC
)

SELECT * FROM top_actors_by_genre 
WHERE rank BETWEEN 1 AND 3
