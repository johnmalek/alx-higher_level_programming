-- Display records using INNER JOIN
-- List all shows in hbtb_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id=tv_show_genres.genre_id ORDER BY tv_shows.title, tv_show_genre.genre_id ASC;

