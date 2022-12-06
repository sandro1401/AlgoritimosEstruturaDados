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
            print('--------------------')         
            aux = self.topo
            while (aux):
                print(f'{aux}') 
               
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
                print('---------------------')         
                aux = self.topo
                while (aux):
                    print(aux) 
                    aux = aux.proximo
                
    def removerDrone(self):
        if self.topo == None:
            print("Pilho vazia\n-------------")
        else:
            self.topo = self.topo.proximo
        self.imprimirDrone()