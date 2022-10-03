class Pessoa:
    def __init__(self, id, nome, fone, end):
        self.id = id
        self.nome = nome
        self.fone = fone
        self.endereco = end
    
    def cadastrar(self, nome, cidade):
        self.nome = nome
        self.endereco.cidade = cidade
    
    def getCidade(self):
        return self.endereco.cidade