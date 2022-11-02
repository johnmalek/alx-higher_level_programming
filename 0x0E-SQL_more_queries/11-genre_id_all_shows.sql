-- Display records using LEFT JOIN
-- List all shows in the database
SELECT tv_shows.title, tv_show_genre.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.genre_id ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;

