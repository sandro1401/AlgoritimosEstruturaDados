from Pessoa import Pessoa


class Juridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, CNPJ, inscricaoEstadual, quantidadeFuncionarios):
        super().__init__(codigo, nome, endereco, telefone)
        self.__CNPJ = CNPJ
        self.__inscricaoEstadual = inscricaoEstadual
        self.quantidadeFuncionarios = quantidadeFuncionarios


    def imprimeCNPJ(self):
        print("CPNJ: ", self.__CNPJ)

    def __emitirNotaFiscal(self, nome, cpf):
        print(f"Nome Empresa:  {self.nome}\n"
        f"CPNJ: {self.__CNPJ}\n"
        f"Inscriçao Estadual: {self.__inscricaoEstadual}\n"
        f"Cliente: {nome}\n"
        f"CPF: {cpf}")
