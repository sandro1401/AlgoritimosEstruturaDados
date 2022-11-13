from Torre import Torre
class Apartamento:
    def __init__(self, id=None, numero=None, torre=None, vaga=None):
        self. id = id
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        self.proximo = None


    def cadastrar(self, id, numero, torre, vaga=None):
        self.id = id
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        self.imprimir()
       
    def imprimir(self):
        print(f"Id: {self.id}\nnúmero: {self.numero}\nTorre: {self.torre}\nVaga: {self.vaga}")
        print("--------------")
