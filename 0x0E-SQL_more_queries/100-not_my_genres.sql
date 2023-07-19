-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT `name`
FROM `tv_genres`
WHERE name NOT IN ( SELECT g.`name`
FROM `tv_genres` AS g
	INNER JOIN `tv_show_genres` AS sg
	ON `sg`.`genre_id` = `g`.`id`
	INNER JOIN `tv_shows` AS s
        ON `sg`.`show_id` = `s`.`id`
	WHERE s.`title` = "Dexter" )
ORDER BY `name`;
