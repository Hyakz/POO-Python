from Heranca.pessoa import Pessoa

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome_classe} está comprando')