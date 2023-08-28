'''
Exercícios Parte 2
Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles.
Depois imprima a soma dos valores.
A string deve ter valor  "1,3,4,6,10,76"
'''

def soma (nums):
    nums = nums.split(',')
    
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    
    soma = 0    
    for i in nums:
        soma += i
    return soma
    
string = "1,3,4,6,10,76"
print(soma(string))