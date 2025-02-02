def category_average_imdb(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb(category_movies) if category_movies else 0

print(category_average_imdb(movies, "Romance")) 