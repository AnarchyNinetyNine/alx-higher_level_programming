-- Script: 10-genre_id_by_show.sql
-- A script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
FROM tv_shows, tv_genre
WHERE tv_show_genres.genre_id IN (
    SELECT genre_id
    FROM tv_show_genres
    WHERE COUNT(genre_id) >= 1
)
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
