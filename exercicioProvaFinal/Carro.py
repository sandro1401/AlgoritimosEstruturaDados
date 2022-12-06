from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca=None, modelo=None, portas= None):
        super().__init__(marca=marca, modelo=modelo)
        self._portas = portas
        self.proximo = None

    def getInformacoes(self):
        return super().getInformacoes() + f"\nPortas: {self._portas}"

    def cadastrar(self, marca, modelo, portas):
        self.marca = marca
        self.modelo = modelo
        self._portas = portas
        