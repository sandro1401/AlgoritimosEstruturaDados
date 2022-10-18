from No import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None



    def adicionarElementosOrdem(self, valor):
        nodo = No(valor)
        if self.inicio == None and self.fim == None:
            self.inicio = nodo 
            self.fim = nodo
        else:
            
            aux = self.inicio
            while (aux.proximo):
                aux = aux.proximo
            aux.proximo = nodo
        self.imprimir()


        
    def imprimir(self):
        if self.inicio == None:
            print("Lista vazia!\n------------")
        else:
            print("------------\n")
            aux = self.inicio
            while (aux):
                print(aux.dado , "\n")
                aux = aux.proximo