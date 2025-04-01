# Código para saber o que foi feito anteriormente;

from Association.escritor import Escritor
from Association.caneta import Caneta
from Association.maquina_escrever import MaquinaEscrever

escritor = Escritor('João')
caneta   = Caneta('Bic')
maquina  = MaquinaEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever() # Executa o método escrever dentro da classe Caneta

##################################################################################

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

##################################################################################

from Composition.clientes import Cliente

c1 = Cliente('João', 20)
c1.inserir_endereco('Bariri', 'SP')

del c1

c2 = Cliente('Maria', 50)
c2.inserir_endereco('Rio de Janeiro', 'RJ')

c3 = Cliente('Luiz', 30)
c3.inserir_endereco('São Paulo', 'SP')

c1.listar_enderecos()
c2.listar_enderecos()
c3.listar_enderecos()

print("############")

##################################################################################

from Heranca.cliente import Cliente
from Heranca.aluno import Aluno
from Heranca.pessoa import Pessoa

c1 = Cliente('Luiz', 23)
a1 = Aluno('Joao', 12)

c1.falar()
c1.comprar()

a1.falar()
a1.estudar()