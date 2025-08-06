/*
In the CTE groups we use a trick to group each players respective winning/losing streak into different groups

We then in CTE streak, count the length of each streak filtering only for wins
and finally we select the player with the longest winning streak 
*/
WITH groups AS (
    SELECT player_id,
        match_result,
        ROW_NUMBER() OVER(ORDER BY player_id, match_date ASC) -
        ROW_NUMBER() OVER(PARTITION BY match_result ORDER BY player_id,match_date ASC) AS grp
    FROM players_results
), streak AS (
    SELECT player_id,
        count(*) AS streak_length
    FROM groups
    WHERE match_result='W'
    GROUP BY player_id, grp
    ORDER BY streak_length DESC
)

SELECT player_id, streak_length FROM streak WHERE streak_length=(SELECT MAX(streak_length) FROM streak)