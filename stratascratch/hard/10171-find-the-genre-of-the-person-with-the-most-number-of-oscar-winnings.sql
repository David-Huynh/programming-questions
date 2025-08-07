WITH count_oscar_wins AS (
    SELECT nominee, count(*) 
    FROM oscar_nominees 
    WHERE winner = TRUE 
    GROUP BY nominee 
    ORDER BY count(*) DESC, nominee ASC 
    LIMIT 1
)

SELECT top_genre FROM count_oscar_wins c JOIN nominee_information n ON c.nominee=n.name