def high_rated_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

print(high_rated_movies(movies))