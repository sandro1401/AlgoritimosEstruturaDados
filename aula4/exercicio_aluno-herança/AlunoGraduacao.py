from Aluno import Aluno

class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
       super().__init__(codigo, nome, matricula)
       self.semestre = semestre

    
    def imprimirAlunoGraduacao(self):
        super().imprimir()
        print(f'Semestre: ', self.semestre)
