from Apartamento import Apartamento

class FilaEspera:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar(self, id, numero, torre):
        apto = Apartamento(id, numero, torre)
        if self.inicio == None:
            self.inicio = apto
            self.fim = apto
        else:
            self.fim.proximo = apto
            self.fim = apto
        self.imprimir()
    
   
    def imprimir(self):
        if self.inicio == None:
            print("Vaga Disponível!!!\n------------")
        else:
            print("--------------\n")
            texto = " "
            aux = self.inicio
            while (aux):
                texto +="Apto nº: "+ str(aux.numero) + " " +aux.torre.nome + " | " 
                aux = aux.proximo
            print(texto)

    
    def remover(self, vaga):
        if self.inicio == None:
            print("Vaga Disponível!!!\n")
        else:
            if self.inicio.proximo == None:
                self.inicio.vaga = vaga
                self.inicio = None
                self.fim = None
            else:
                self.inicio.vaga = vaga
                self.inicio = self.inicio.proximo
            self.imprimir()