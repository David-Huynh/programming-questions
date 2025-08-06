/*
Selects the user IDs of users who have logged in for three consecutive days.
*/
SELECT user_id 
FROM sf_events s1
WHERE (
    SELECT user_id 
    FROM sf_events s2 
    WHERE s2.user_id=s1.user_id 
    AND s2.record_date=s1.record_date + INTERVAL '1 day') IS NOT NULL 
AND (SELECT user_id 
    FROM sf_events s3 
    WHERE s3.user_id=s1.user_id 
    AND s3.record_date=s1.record_date + INTERVAL '2 day') IS NOT NULL


