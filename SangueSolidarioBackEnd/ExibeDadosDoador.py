from ServicoDoador import ServicoDoador

class ExibeDadosDoador(ServicoDoador):
    def __init__(self, doador=None):
        super().__init__()
        self.__doador = doador

    def execute(self):
        return self.__doador