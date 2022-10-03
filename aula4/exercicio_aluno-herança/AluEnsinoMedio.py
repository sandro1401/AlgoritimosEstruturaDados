from Aluno import Aluno


class AluEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
       super().__init__(codigo, nome, matricula)
       self.ano = ano


    def imprimirAluEnsinoMedio(self):
        super().imprimir()
        print(f'Ano: ', self.ano)

