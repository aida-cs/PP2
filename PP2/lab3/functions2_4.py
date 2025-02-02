def average_imdb(movies):
    return sum(movie["imdb"] for movie in movies) / len(movies)

print(average_imdb(movies))