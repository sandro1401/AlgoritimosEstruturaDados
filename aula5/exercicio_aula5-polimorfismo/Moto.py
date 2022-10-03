from tokenize import Double
from xmlrpc.client import boolean
from Automovel import Automovel

class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade= 0, potenciaDoMotor = Double, partidaEletrica = boolean):
        super().__init__(marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.partidaEletrica = partidaEletrica
    
    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print("Partidade Eletrica: ", self.partidaEletrica)
