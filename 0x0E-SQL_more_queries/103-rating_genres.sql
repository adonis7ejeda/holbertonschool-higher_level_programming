-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
-- SQL is fun
select tv_genres.name, SUM(tv_show_ratings.rate) AS rating
from tv_genres inner join tv_show_genres
on tv_genres.id = tv_show_genres.genre_id
inner join tv_shows
on tv_shows.id = tv_show_genres.show_id
inner join tv_show_ratings
on tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
