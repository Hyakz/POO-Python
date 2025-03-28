class BaseDeDados: 
    def __init__(self):
        # self._dados = {} # _dados é um atributo protegido, só pode ser acessado dentro da classe e em subclasses
        self.__dados = {} # __dados é um atributo privado, só pode ser acessado dentro da classe 
        
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})         
        
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
        
    def apaga_cliente(self, id):
        del self.__dados['clientes'][id] # del = deleta um item do dicionario (dados), (coluna clientes), (apagando pelo id)s