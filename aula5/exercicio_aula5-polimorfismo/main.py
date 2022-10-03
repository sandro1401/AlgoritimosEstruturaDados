from Veiculo import Veiculo
from Automovel import Automovel
from Carro import Carro
from Moto import Moto
from Bicicleta import Bicicleta

v = Veiculo("Fiat", 4, "Marrea", 80)
v.acelerar(40)
v.frear(20)

v.imprimirInformacoes()

c = Carro("ford", 4, "Ka", 60, "1.8", 4)
c.acelerar(30)
c.frear(20)
c.imprimirInformacoes()

m = Moto("Honda", 2, "PCX", 90,"1.0", True)
m.acelerar(20)
m.frear(10)
m.imprimirInformacoes()

b = Bicicleta("Caloi", 2, "Cross", 50, 18, False)
b.acelerar(10)
b.frear(5)
b.imprimirInformacoes()