from tokenize import Double
from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade= 0, potenciaDoMotor = Double, qdtPortas = None):
        super().__init__(marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.qdtPortas = qdtPortas
    
    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print("Qtd Portas: ", self.qdtPortas)
