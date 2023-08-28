'''
Exercícios Parte 2
Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
Dica: leia a documentação do pacote json
'''

import json

with open('person.json') as arquivo:
    conteudo = arquivo.read()

dados = json.loads(conteudo)

print(dados)
