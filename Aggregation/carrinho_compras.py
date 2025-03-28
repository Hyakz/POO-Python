class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
        
    def inserir_produto(self, produto):
        self.produtos.append(produto)
    
    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)
    
    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        
        return print(total)