class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def imprimir(self):
        print(f"Código: {self.codigo}\n"
        f"Nome:  {self.nome}\n"
        f"Núm da matricula: {self.matricula}")
