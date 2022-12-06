from Livro import Livro

class Pilha:
    def __init__(self):
        self.topo = None

    def adicionarLivro(self, livro):
        if self.topo == None:
            self.topo = livro
        else:
            livro.proximo = self.topo
            self.topo = livro
        self.imprimir()

    def imprimir(self):
        if self.topo == None:
            print('Pilha vazia!')
        else:
            aux = self.topo
            while aux:
                print(aux)
                aux = aux.proximo
