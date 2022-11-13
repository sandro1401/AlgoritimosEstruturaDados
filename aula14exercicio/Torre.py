class Torre:
    def __init__(self, id=None, nome=None, endereco=None):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        

    def cadastrar(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def imprimir(self):
        print(f"Id: {self.id}\nnome: {self.nome}\nendereço: {self.endereco}")
        print("----------------")
