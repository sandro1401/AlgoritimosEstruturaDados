from tokenize import Double
from Pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso = Double, altura= Double):
        super().__init__(codigo, nome, endereco, telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura


    def imprimiCPF(self):
        print("CPF: ", self.__cpf)
        print('------------------')
        
    
    def __calculaIMC(self):
        print("IMC: ", (self.peso/(self.altura * 2)))
        print('------------------')

    def IMC(self):
        return self.__calculaIMC()