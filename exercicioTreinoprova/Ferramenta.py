from abc import ABCMeta, abstractmethod

class Ferramenta(metaclass=ABCMeta):
    def __init__(self, nome= None, tensao= None, preco= None):
        self.nome = nome
        self.tensao = tensao
        self.preco = preco


    def getInformacoes(self):
        return f"Nome: {self.nome}\nTensão: {self.tensao}\nPreço: {self.preco}"

    @abstractmethod
    def cadastrar(self):
        pass
