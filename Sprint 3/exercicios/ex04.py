'''
Exercícios Parte 1
Escreva um código Python para imprimir todos os números primos entre 1 até 100.
Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.
Importante: Aplique a função range().
'''

def primo(num):
    if num == 1:
        return False
    resto0 = 0
    for i in range(1, num):
        if num % i == 0:
            resto0 += 1
    if resto0 == 1:
        return True
    else:
        return False


for i in range(1, 101):
    if primo(i):
        print(i)
