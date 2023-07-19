--  lists all records of the table second_table that have name
SELECT `score`, `name`
FROM `second_table`
WHERE name != ''
ORDER BY score DESC;
