# [Warm up] Em Python, declare e inicialize uma lista contendo o nome de 20 animais.
# Ordene-os em ordem crescente e itere sobre os itens, imprimindo um a um
#(você pode utilizar list comprehension aqui).  Na sequência, armazene o conteúdo da
# lista em um arquivo de texto, um item em cada linha, no formato CSV.

animais = ['cachorro', 'gato', 'coelho', 'porco', 'galinha',
           'vaca', 'ovelha', 'elefante', 'girafa', 'tigre',
           'zebra', 'rinoceronte', 'macaco', 'canguru', 'urso',
           'lobo', 'raposa', 'panda', 'pinguim', 'crocodilo']

animais.sort()

[print(animal) for animal in animais]

with open("animais.csv", "w") as arquivo:
    for animal in animais:
        arquivo.write(animal + "\n")
