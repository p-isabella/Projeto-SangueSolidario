from abc import ABC, abstractmethod

class ServicoDoador(ABC):
    # Interface que algoritmos concretos devem implementar

    @abstractmethod
    def __init__(self, doador=None):
        self.__doador = doador

    @abstractmethod
    def execute(self):
        pass