class Cidade:
    def __init__(self, id, nome, uf):
        self.id = id
        self.nome = nome
        self.uf = uf

    def __str__(self):
        return f"ID Cidade: {self.id} - Nome Cidade: {self.nome} - UF: {self.uf}"