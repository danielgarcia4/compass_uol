# [Warm up]  Em Python, declare e inicialize uma lista contendo 250 inteiros obtidos de forma aleatória.
# Após, aplicar o método reverse sobre o conteúdo da lista e imprimir o resultado.

import random

lista = [random.randint(1,1000) for x in range(250)]

print(lista)

lista.reverse()

print(lista)
