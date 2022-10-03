class Endereco:
    def __init__(self, id, logradouro, cidade):
        self.id = id
        self.logradouro = logradouro
        self.cidade = cidade

    def imprimir(self):
        print(f"Cidade: {self.cidade} - Endereço: {self.logradouro}")

