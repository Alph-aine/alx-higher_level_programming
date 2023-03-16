-- select a score, count number of occurences and groups them
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY  number DESC;
