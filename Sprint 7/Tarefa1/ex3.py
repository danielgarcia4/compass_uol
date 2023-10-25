# Apresente o nome do ator/atriz com a maior média por filme.

import pandas as pd

df = pd.read_csv('actors.csv')

ator = df[df['Average per Movie'] == df['Average per Movie'].max()]

nome_ator = ator['Actor'].values[0]

print(f"O ator/atriz com a maior media por filme: {nome_ator}.")