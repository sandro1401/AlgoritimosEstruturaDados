from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo = "Fusco", nPortas = 4):
        super().__init__(modelo=modelo)
        self.nportas = nPortas

    
    def imprimir(self):
        super().imprimir()
        print("Qtd: ", self.nportas)

    
    def __str__(self):
        return super().__str__() +"\nQtd Portas: " + str(self.nportas)

        