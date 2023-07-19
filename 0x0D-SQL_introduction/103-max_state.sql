-- print top 3 city in temp in during July and August
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `max_temp` DESC
