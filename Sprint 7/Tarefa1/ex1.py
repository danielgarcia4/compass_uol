# Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.

import pandas as pd

df = pd.read_csv('actors.csv')

ator = df[df['Number of Movies'] == df['Number of Movies'].max()]

nome_ator = ator['Actor'].values[0]

n_filmes = ator['Number of Movies'].values[0]

print(f"O ator com mais filmes: {nome_ator}. Participou de {n_filmes} filmes.")