class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__ # Pega o nome da classe usada no momento 
        
    def falar(self):
        print(f'{self.nome_classe} está falando')