'''
Exercícios Parte 1
Implemente duas classes, Pato e Pardal , que herdam de uma superclasse
chamada Passaro as habilidades de voar e emitir som.
Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console,
conforme o modelo a seguir. Imprima no console exatamente assim:
Pato
Voando...
Pato emitindo som...
Quack Quack
Pardal
Voando...
Pardal emitindo som...
Piu Piu
'''

class Passaro:
    def __init__(self, especie):
        self.especie = especie
    
    def voar(self):
        print("Voando...")
    
    def emitir_som(self):
        print(self.especie + " emitindo som...")
        
class Pato(Passaro):
    def __init__(self):
        super().__init__("Pato")
    def emitir_som(self):
        super().emitir_som()
        print("Quack Quack")
        
class Pardal(Passaro):
    def __init__(self):
        super().__init__("Pardal")
    def emitir_som(self):
        super().emitir_som()
        print("Piu Piu")
        
pato = Pato()
pardal = Pardal()

print(pato.especie)
pato.voar()
pato.emitir_som()

print(pardal.especie)
pardal.voar()
pardal.emitir_som()
