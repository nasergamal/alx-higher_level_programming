-- script that lists all shows, and all genres linked to that show.
SELECT `s`.`title`, g.`name`
FROM `tv_shows` AS s
	LEFT OUTER JOIN (`tv_show_genres` AS sg
	INNER JOIN `tv_genres` AS g
        ON `sg`.`genre_id` = `g`.`id`)
	ON `sg`.`show_id` = `s`.`id`
ORDER BY s.`title`, g.`name`;
