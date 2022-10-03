from tokenize import Double
from Veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade= 0, potenciaDoMotor = Double):
        super().__init__(marca, qtdRodas, modelo, velocidade)
        self.potenciaDoMotor = potenciaDoMotor


    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print("Potencia do Motor: ", self.potenciaDoMotor)