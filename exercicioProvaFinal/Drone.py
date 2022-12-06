from Veiculo import Veiculo

class Drone(Veiculo):
    def __init__(self, marca=None, modelo=None, helices= None):
        super().__init__(marca=marca, modelo=modelo)
        self.__helices = helices
        self.proximo = None

    def getInformacoes(self):
        return super().getInformacoes() + f"\nQuantidades de Helices: {self.__helices}"

    def cadastrar(self, marca, modelo, helices):
        self.marca = marca
        self.modelo = modelo
        self.__helices = helices
        