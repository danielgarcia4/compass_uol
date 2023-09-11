'''
E2
Utilizando high order functions, implemente o corpo da função conta_vogais.
O parâmetro de entrada será uma string e o resultado deverá ser a contagem de
vogais presentes em seu conteúdo.
É obrigatório aplicar as seguintes funções: len, filter, lambda
Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.
'''

def conta_vogais(texto:str)-> int:
    texto = texto.lower()
    vogais = lambda x: x in 'aeiou'
    qtd_vogais = filter(vogais, texto)
    sum_vogais = len(list(qtd_vogais))
    return sum_vogais
    
if __name__ == '__main__':
    entrada = input("Digite uma palavra: ")
    print(conta_vogais(entrada))