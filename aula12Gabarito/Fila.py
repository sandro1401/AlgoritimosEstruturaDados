from Carro import Carro

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    
    def add(self, placa, km):
        no = Carro(placa, km)
        if self.inicio == None:
            self.inicio = no
            self.fim = no
        else:
            self.fim.proximo = no
            self.fim = no
        self.imprimir()

    def imprimir(self):
            if self.inicio == None:
                print("Fila de Carros vazia!\n------------")
            else:
                print("------------\n")
                texto = " "
                aux = self.inicio
                while (aux):
                    texto +=  aux.placa + ": " + str(aux.km) + "Km | " 
                    aux = aux.proximo
                print(texto)

    def remover(self):
        if self.inicio == None:
            print("Fila de Carros vazia\n-------------")
        else:
            if self.inicio.proximo == None:
                self.inicio = None
                self.fim = None
            else:
                self.inicio = self.inicio.proximo
            self.imprimir()