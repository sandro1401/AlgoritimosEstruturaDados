from abc import ABCMeta, abstractmethod

class Veiculo(metaclass=ABCMeta):
    def __init__(self, marca= None, modelo= None):
        self.marca = marca
        self.modelo = modelo
       

    def getInformacoes(self):
        return f"marca: {self.marca}\nmodelo: {self.modelo}"

    @abstractmethod
    def cadastrar(self):
        pass

    def __str__(self):
        return f"marca: {self.marca}\nModelo: {self.modelo}"