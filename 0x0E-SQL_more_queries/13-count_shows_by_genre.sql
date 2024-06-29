SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) As number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres