from Livro import Livro

class Pilha:
    def __init__(self):
        self.topo = None
       

    def add(self, titulo):
        livro = Livro(titulo)
        if self.topo == livro:
            self.topo = livro
        else:
            livro.proximo = self.topo
            self.topo = livro
        self.imprimir()

    def imprimir(self):
            if self.topo == None:
                print("Pilha de Livros vazia!\n------------")
            else:
                print("------------\n")
                
                aux = self.topo
                while (aux):
                    print(aux.titulo, "\n") 
                    aux = aux.proximo
                
    def remover(self):
        if self.topo == None:
            print("Pilho vazia\n-------------")
        else:
            # if self.topo.proximo == None:
            #     self.proximo = None
            #     self.topo = None
            # else:
            self.topo = self.topo.proximo
        self.imprimir()