from Ferramenta import Ferramenta

class Furadeira(Ferramenta):
    def __init__(self, nome=None, tensao=None, preco=None, potencia = None):
        super().__init__(nome, tensao, preco)
        self._potencia = potencia

    def getInformacoesFuradeira(self):
        return super().getInformacoes() + f"\nPotencia: {self._potencia}"

    def cadastrar(self, nome, tensao, preco, potencia):
        self.nome = nome
        self.tensao = tensao
        self.preco = preco
        self._potencia = potencia