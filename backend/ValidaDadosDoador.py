from ServicoDoador import ServicoDoador

class ValidaDadosDoador(ServicoDoador):
    # Algoritmo concreto de Validação dos Dados

    def __init__(self, doador=None):
        super().__init__()
        self.__doador = doador

    def execute(self):
        if self.__doador is None:
            return False
        return True