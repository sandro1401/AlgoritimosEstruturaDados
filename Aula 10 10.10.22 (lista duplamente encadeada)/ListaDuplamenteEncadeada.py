from No import No

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        # self.fim = None
       

    def adicionarOrdemAlfabetica(self, valor):
        if self.inicio == None:
            print("Lista Vazia!!!")
            nodo = No(valor)
            self.inicio = nodo
            return
        else:
            ordemAlfabeticaAtual = ord(self.inicio.dado)
            ordemAlfabeticaNovo = ord(valor)

            if ordemAlfabeticaNovo < ordemAlfabeticaAtual:
                nodo = No(valor)
                self.inicio.proximo = nodo
                nodo.ant = self.inicio 
                self.inicio = nodo
            elif ordemAlfabeticaNovo > ordemAlfabeticaAtual:
                nodo = No(valor)
                nodo.proximo = self.inicio 
                self.inicio.ant = nodo 
                self.inicio = nodo



        # if self.inicio == None:
        #     self.inicio = nodo
        # else:
        #     aux = self.inicio
        #     while aux.proximo < valor:
        #         aux = aux.proximo
        #     aux.proximo = nodo
        # self.imprimir()
    
    def adicionarNoFim(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
        else:
            aux = self.inicio
            while aux.proximo:
                aux = aux.proximo
            aux.proximo = nodo
        self.imprimir()

    def adicionarNoInicio(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
        else:
            nodo.proximo = self.inicio
            self.inicio = nodo
        self.imprimir()

#Para ordem inversa, inicia no fim e aponta para o anterior
    def imprimir(self):
        if self.inicio == None:
            print("Lista vazia!\n-----------")
        else:
            print("-----------\n")
            aux = self.inicio
            while (aux):
                print(aux.dado , "\n")
                aux = aux.proximo
                                
               

    def removerDoInicio(self):
        if self.inicio == None:
            print("Lista vazia!\n-----------")
        elif self.inicio.proximo == None:
            self.inicio = None
        else:
            self.inicio = self.inicio.proximo
        self.imprimir()

    def removerDoFim(self):
        if self.inicio == None:
            print("Lista vazia!\n-----------")
        elif self.inicio.proximo == None:
            self.inicio = None
        else:
            ant = self.inicio
            aux = self.inicio.proximo
            while aux.proximo:
                ant = aux
                aux = aux.proximo
            ant.proximo = None
        self.imprimir()