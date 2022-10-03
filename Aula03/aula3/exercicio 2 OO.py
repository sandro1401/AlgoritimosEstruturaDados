
"""Exercício
▷ Construa um algoritmo para implementar a
classe Retângulo que possui os atributos: altura
e largura.
▷ A classe deve ter os seguintes métodos:
○ Método construtor
○ Método que calcula a área do retângulo
( altura * largura) e retorna o resultado
○ Método que imprime os valores dos atributos
da classe."""


class Retangulo:
    def __init__(self, altura, largura):
        self.__altura = altura
        self.__largura = largura
        self.__area = 0

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    @property
    def largura(self):
        return self.__largura

    @largura.setter
    def largura(self, largura):
        self.__largura = largura

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.__area = area

    def calculo_area(self):
        self.__area = self.__altura * self.__largura
        return self.__area

    def __str__(self):
        return f"Altura: {self.__altura} - Largura: {self.__largura} - Area: {self.__area} "


def dados():
    altura = int(input(f"informe a altura do Retângulo: "))
    largura = int(input(f"Informe a largura do Retângulo: "))
    retangulo = Retangulo(altura, largura)
    retangulo.calculo_area()
    print(f" {retangulo}")


dados()