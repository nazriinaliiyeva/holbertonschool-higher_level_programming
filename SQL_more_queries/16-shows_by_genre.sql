-- show by genre
SELECT tv_shows.title, tv_genres.name
FROM tv_shows 
INNER JOIN tv_show_genres on tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres on tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC,tv_genres.name ASC;
