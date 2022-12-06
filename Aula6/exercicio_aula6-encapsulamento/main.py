from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica


p1 = Pessoa(1,"João", "Rua 1", "5199999999")
p1.imprimirNome()

f1 = Fisica(2, "Pedro", "Rua 2", "5198798798", "62626262626", 18, 78, 1.74)
f1.imprimiCPF()
f1.IMC()

j1 = Juridica(1, "RM", "Rua 3", "513388788", "75-3535354/0001-45", "85848748", 1)
j1.imprimeCNPJ()
j1.cupomfiscal()