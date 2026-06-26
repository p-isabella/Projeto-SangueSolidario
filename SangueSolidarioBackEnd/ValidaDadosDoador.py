from ServicoDoador import ServicoDoador

class ValidaDadosDoador(ServicoDoador):
    # Algoritmo concreto de Validação dos Dados
    def execute(self, doador) -> bool:
        if doador is None:
            return False
        return True