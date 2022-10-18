from No import No

class ListaDuplamenteEncadeada:
    def __init__(self):
        # self.inicio = None
        # self.fim = None
        self.ponteiro = None

    def adicionarOrdemAlfabetica(self, valor):
        if not self.ponteiro:
            nodo = No(valor)
            self.ponteiro = nodo
            return
        ordemAlfabeticaAtual = ord(self.ponteiro.dado)
        ordemAlfabeticaNovo = ord(valor)

        if ordemAlfabeticaNovo > ordemAlfabeticaAtual:
             nodo = No(valor)
             self.ponteiro.prox = nodo
             nodo.ant = self.ponteiro 
             self.ponteiro = nodo
        elif ordemAlfabeticaNovo < ordemAlfabeticaAtual:
             nodo = No(valor)
             nodo.prox = self.ponteiro 
             self.ponteiro.ant = nodo 
             self.ponteiro = nodo



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
        if self.ponteiro == None:
            print("Lista vazia!\n-----------")
        else:
            print("-----------\n")
            aux = self.ponteiro
            while aux.ant:
                self.ponteiro = aux.ant
                
            while aux.prox:
                print(aux.dado)
                self.ponteiro = aux.prox
             

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