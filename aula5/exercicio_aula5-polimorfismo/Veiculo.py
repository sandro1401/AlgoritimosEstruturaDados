class Veiculo:
    def __init__(self, marca, qtdRodas, modelo, velocidade= 0):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade

    def imprimirInformacoes(self):
        print("Marca: " , self.marca, "\nqtdRodas: ", self.qtdRodas, "\nModelo:" , self.modelo, "\nvelocidade :" , self.velocidade )

    
    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        self.velocidade -= valor

    
