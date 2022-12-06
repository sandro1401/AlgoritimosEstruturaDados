from Ferramenta import Ferramenta
from Furadeira import Furadeira

class Lixadeira(Ferramenta):
    def __init__(self, nome=None, tensao=None, preco=None, potencia = None, rotacoes= None ):
        super().__init__(nome, tensao, preco)
        self._potencia = potencia
        self.__rotacoes = rotacoes

    
    def getInformacoesLixadeira(self):
        return super().getInformacoes() + f"\nPotencia: {self._potencia}\nRotaçoes por Min: {self.__rotacoes}"
       
    
    def cadastrar(self, nome, tensao, preco, potencia, rotacoes):
        self.nome = nome
        self.tensao = tensao
        self.preco = preco
        self._potencia = potencia
        self.__rotacoes = rotacoes