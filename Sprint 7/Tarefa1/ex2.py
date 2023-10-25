# Apresente a média da coluna contendo o número de filmes.

import pandas as pd

df = pd.read_csv('actors.csv')

media_number_of_movies = df['Number of Movies'].mean()

print(media_number_of_movies)