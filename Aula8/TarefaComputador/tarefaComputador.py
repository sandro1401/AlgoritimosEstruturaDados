
# Computador
from abc import ABCMeta, abstractmethod

class Computador(metaclass=ABCMeta):
    def __init__(self, modelo = None, cor = None, preco = None):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    def getInformacoes(self):
       return f"Modelo: {self.modelo}\n cor: {self.cor}\n Preço: {self.preco}"
       
    @abstractmethod
    def cadastrar(self):
        pass



# Desktop
from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo = None, cor = None, preco = None, potenciaDaFonte = None):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        return super().getInformacoes() + f"\nPotencia da Fonte: {self._potenciaDaFonte}"
    
    def cadastrar(self, modelo, cor, preco, potenciaDaFonte):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self._potenciaDaFonte = potenciaDaFonte



# Notebook
from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo = None, cor = None, preco = None, tempoDeBateria = None):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria
    
    def getInformacoes(self):
        return super().getInformacoes() + f"\nTempo de Bateria: {self.__tempoDeBateria}"

    def cadastrar(self, modelo, cor, preco, tempoDeBateria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.__tempoDeBateria = tempoDeBateria




# main
from Desktop import Desktop
from Notebook import Notebook

note = Notebook()
note.cadastrar("Asus", "preto", 1000, "10 hs")
print(note.getInformacoes())

desk = Desktop()
desk.cadastrar("Dell", "Prata", 3000, "500 Watts")
print(desk.getInformacoes())