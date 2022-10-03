from xmlrpc.client import boolean
from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade=0, numMarchas = None, bagageiro = boolean):
        super().__init__(marca, qtdRodas, modelo, velocidade)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print("Número de Marchas: ", self.numMarchas,
        "\nBagageiro: ", self.bagageiro)
