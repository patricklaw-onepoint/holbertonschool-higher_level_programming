-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
--   Each record should display: tv_shows.title - rating sum
--   Results must be sorted in descending order by the rating
-- run: cat 102-rating_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;