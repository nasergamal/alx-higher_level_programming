-- Lists records with score higher than 10 from the table
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
