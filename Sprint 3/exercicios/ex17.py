'''
Exercícios Parte 2
Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas:
a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
'''

def tres_listas(lista):
    tamanho = len(lista)
    tamanho_partes = int(tamanho/3)
    
    parte1 = lista[:tamanho_partes]
    parte2 = lista[tamanho_partes:tamanho_partes*2]
    parte3 = lista[tamanho_partes*2:]
  
    return parte1, parte2, parte3


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

parte1, parte2, parte3 = tres_listas(lista)

print(parte1, parte2, parte3)
