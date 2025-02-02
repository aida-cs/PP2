def is_high_rated(movie):
    return movie["imdb"] > 5.5

print(is_high_rated(movies[0]))