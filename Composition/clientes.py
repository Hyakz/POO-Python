from Composition.endereco import Endereco

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = [] # Receber da classe endereço
        
    def inserir_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))
        
    def listar_enderecos(self):
        for e in self.enderecos:
            print(e.cidade, e.estado)
            
    def __del__(self):
        print(f'{self.nome} foi apagado!')