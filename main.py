# Código comentado para saber o que foi feito anteriormente;

# from Association.escritor import Escritor
# from Association.caneta import Caneta
# from Association.maquina_escrever import MaquinaEscrever

# escritor = Escritor('João')
# caneta   = Caneta('Bic')
# maquina  = MaquinaEscrever()

# escritor.ferramenta = caneta
# escritor.ferramenta.escrever() # Executa o método escrever dentro da classe Caneta

from Aggregation.carrinho_compras import CarrinhoDeCompras
from Aggregation.produto import Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 69.99)
p2 = Produto('Calça Jeans', 189.99)
p3 = Produto('Boné', 49.99)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.listar_produtos()

carrinho.soma_total()
