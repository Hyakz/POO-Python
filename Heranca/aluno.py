from Heranca.pessoa import Pessoa

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome_classe} está estudando')