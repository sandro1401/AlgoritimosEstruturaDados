class Pessoa:
    def __init__(self, codigo, nome, end, fone):
        self.codigo = codigo
        self.nome = nome
        self.endereco = end
        self.fone = fone
        
    def imprimir(self):
        print("Nome: " , self.nome)
        print("End: " , self.endereco)


class Fisica(Pessoa):
    def __init__(self, codigo, nome, end, fone, cpf):
        super().__init__(codigo, nome, end, fone)
        self.cpf = cpf 