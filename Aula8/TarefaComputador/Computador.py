# Construir código necessário em Python para implementar o seguinte projeto:
#  Uma classe abstrata chamada de Computador que contém os atributos/propriedades: modelo, cor e preço.
#  Esta classe possui um método getInformacoes() que retorna todos os valores dos atributos.
#  Esta classe também possui um método abstrato cadastrar().
 

# O projeto também deve possuir as classes Desktop e Notebook que herdam da classe Computador.
#  A classe Desktop possui o atributo/propriedade fracamente privado potenciaDaFonte. 
# Esta classe reimplementa o método getInformacoes() herdado de computador.
 

# A classe Notebook possui o atributo/propriedade fortemente privado tempoDeBateria. 
# Esta classe reimplementa o método getInformacoes() herdado de computador.
 

# Construa um arquivo do tipo main com a utilização das classes construídas, para teste dos algoritmos.

from abc import ABCMeta, abstractmethod


class Computador(metaclass=ABCMeta):
    def __init__(self, modelo = None, cor = None, preco = None):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    def getInformacoes(self):
       return f"Modelo: {self.modelo}\ncor: {self.cor}\nPreço: {self.preco}"
       
    @abstractmethod
    def cadastrar(self):
        pass

