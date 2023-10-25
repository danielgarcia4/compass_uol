#Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

import pandas as pd

df = pd.read_csv('actors.csv')

filmes = df["#1 Movie"].value_counts()

print("Os filmes mais frequentes e suas respectivas frequencias: ")

print(filmes.head(5))
