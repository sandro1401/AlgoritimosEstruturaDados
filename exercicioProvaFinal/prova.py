from abc import ABCMeta, abstractmethod

class Veiculo(metaclass=ABCMeta):
    def __init__(self, marca= None, modelo= None):
        self.marca = marca
        self.modelo = modelo
       

    def getInformacoes(self):
        return f"marca: {self.marca}\nmodelo: {self.modelo}"

    @abstractmethod
    def cadastrar(self):
        pass

    def __str__(self):
        return f"marca: {self.marca}\nModelo: {self.modelo}"


from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca=None, modelo=None, portas= None):
        super().__init__(marca=marca, modelo=modelo)
        self._portas = portas
        self.proximo = None

    def getInformacoes(self):
        return super().getInformacoes() + f"\nPortas: {self._portas}"

    def cadastrar(self, marca, modelo, portas):
        self.marca = marca
        self.modelo = modelo
        self._portas = portas



from Veiculo import Veiculo

class Drone(Veiculo):
    def __init__(self, marca=None, modelo=None, helices= None):
        super().__init__(marca=marca, modelo=modelo)
        self.__helices = helices
        self.proximo = None

    def getInformacoes(self):
        return super().getInformacoes() + f"\nQuantidades de Helices: {self.__helices}"

    def cadastrar(self, marca, modelo, helices):
        self.marca = marca
        self.modelo = modelo
        self.__helices = helices
        

from Carro import Carro
from Drone import Drone


class Pilha:
    def __init__(self):
        self.topo = None
       

    def addCarro(self, carro):
        if self.topo == None:
            self.topo = carro
        else:
            carro.proximo = self.topo
            self.topo = carro
        self.imprimirCarro()

    def imprimirCarro(self):
        if self.topo == None:
            print("Pilha de Carros vazia!\n------------")
        else:
            print("------------\n")
            
            aux = self.topo
            while (aux):
                print(aux)
                print('--------------------') 
                aux = aux.proximo
                
    def removerCarro(self):
        if self.topo == None:
            print("Pilho vazia\n-------------")
        else:
            self.topo = self.topo.proximo
        self.imprimirCarro()


    def addDrone(self, drone):
        if self.topo == drone:
            self.topo = drone
        else:
            drone.proximo = self.topo
            self.topo = drone
        self.imprimirDrone()

    def imprimirDrone(self):
            if self.topo == None:
                print("Pilha de Drones vazia!\n------------")
            else:
                print("------------\n")
                
                aux = self.topo
                while (aux):
                    print(aux) 
                    print('-----------------------')
                    aux = aux.proximo
                
    def removerDrone(self):
        if self.topo == None:
            print("Pilho vazia\n-------------")
        else:
            self.topo = self.topo.proximo
        self.imprimirDrone()




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
        