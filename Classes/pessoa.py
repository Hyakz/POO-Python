from random import randint

class Pessoa:
    ano_atual = 2025
    
    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True
        
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        
        print(f'{self.nome} parou de comer')
        self.comendo = False
        
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
        
    @classmethod # Não pode ser utilizada a Instancia (self)
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod # Não pode ser utilizada a Classe (cls) ou a Instancia (self)
    def gera_id():
        rand = randint(0, 10000)
        return rand