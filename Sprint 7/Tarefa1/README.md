# Sprint 7

##  Tarefa 1

### Exercício 1

```python
# Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.

import pandas as pd

df = pd.read_csv('actors.csv')

ator = df[df['Number of Movies'] == df['Number of Movies'].max()]

nome_ator = ator['Actor'].values[0]

n_filmes = ator['Number of Movies'].values[0]

print(f"O ator com mais filmes é {nome_ator}. Ele participou de {n_filmes} filmes.")
```

``` python
# Resultado:
O ator com mais filmes: Robert DeNiro. Participou de 79 filmes.
```

### Exercício 2

``` python
# Apresente a média da coluna contendo o número de filmes.

import pandas as pd

df = pd.read_csv('actors.csv')

media_number_of_movies = df['Number of Movies'].mean()

print(media_number_of_movies)
```

``` python
# Resultado
37.88 
```

### Exercicio 3

``` python 
# Apresente o nome do ator/atriz com a maior média por filme.

import pandas as pd

df = pd.read_csv('actors.csv')

ator = df[df['Average per Movie'] == df['Average per Movie'].max()]

nome_ator = ator['Actor'].values[0]

print(f"O ator/atriz com a maior media por filme: {nome_ator}.")
```

``` python
# Resultado:
O ator/atriz com a maior media por filme: Anthony Daniels.
```

### Exercício 4

``` python
#Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

import pandas as pd

df = pd.read_csv('actors.csv')

filmes = df["#1 Movie"].value_counts()

print("Os filmes mais frequentes e suas respectivas frequencias: ")

print(filmes.head(5))
```

``` 
## Resultado

Os filmes mais frequentes e suas respectivas frequencias: 
#1 Movie
The Avengers                           6
Catching Fire                          4
Harry Potter / Deathly Hallows (P2)    4
Star Wars: The Force Awakens           3
The Dark Knight                        3
Name: count, dtype: int64
```