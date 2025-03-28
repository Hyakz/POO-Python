from Classes.pessoa import Pessoa
from Classes.produto import Produto
from Classes.dados import BaseDeDados

from Association.escritor import Escritor
from Association.caneta import Caneta
from Association.maquina_escrever import MaquinaEscrever

escritor = Escritor('João')
caneta = Caneta('Bic')
maquina = MaquinaEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever() # Executa o método escrever dentro da classe Caneta