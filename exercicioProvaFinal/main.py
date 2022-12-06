from Carro import Carro
from Drone import Drone
from Pilha import Pilha


c1 = Carro()
c1.cadastrar("Chevrolet", "Celta", 4)
c2 = Carro()
c2.cadastrar("Chevrolet", "Onix", 4)
c3 = Carro()
c3.cadastrar("Rennault", "Clio", 4)
print(c1.getInformacoes())
print(c2.getInformacoes())
print(c3.getInformacoes())

carros = Pilha()
carros.imprimirCarro()

carros.addCarro(c1)
carros.addCarro(c2)
carros.addCarro(c3)
carros.imprimirCarro()
carros.removerCarro()
carros.removerCarro()
carros.removerCarro()


d1 = Drone()
d1.cadastrar("Honda", "M1", 6)
d2 = Drone()
d2.cadastrar("Honda", "M2", 4)
d3 = Drone()
d3.cadastrar("Honda", "M3", 8)
print(d1.getInformacoes())
print(d2.getInformacoes())
print(d3.getInformacoes())

drones = Pilha()
drones.imprimirDrone()

drones.addDrone(d1)
drones.addDrone(d2)
drones.addDrone(d3)
drones.imprimirDrone()
drones.removerDrone()
drones.removerDrone()
drones.removerDrone()