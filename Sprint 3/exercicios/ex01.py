'''
Exercícios Parte 1
Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa.
Como saída, imprima o ano em que a pessoa completará 100 anos de idade.
'''

import datetime

def cemanos(idade):
    diferenca = 100-idade
    ano = datetime.datetime.now().year+diferenca
    return ano
    
nome = input()
idade = int(input())

print(cemanos(idade))
