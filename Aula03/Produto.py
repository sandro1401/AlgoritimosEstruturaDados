#from Categoria import Categoria

class Produto:
    def __init__(self,nome,preco,cat):
        self.id = None
        self.nome = nome
        self.preco = preco
        self.categoria = cat

    def imprimir(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: {self.preco}")
        print(f"Categoria: {self.categoria.nome}")
        print("----------------------")