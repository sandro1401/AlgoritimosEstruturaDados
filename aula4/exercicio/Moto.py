from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marcaMot, anoMot, partida):
        super().__init__(marcaMot, anoMot)
        self.partidaEletrica = partida
        print("Moto Construído")