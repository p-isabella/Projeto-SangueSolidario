from abc import ABC, abstractmethod
from DoadorConcreto import DoadorConcreto

class ServicoDoador(DoadorConcreto):
    def __init__(self, doador=None):
        self._doador = doador

    @abstractmethod
    def execute(self):
        pass