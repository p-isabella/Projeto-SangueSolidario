from abc import ABC, abstractmethod

class ServicoDoador(ABC):
    # Interface que algoritmos concretos devem implementar
    @abstractmethod
    def execute(self, doador):
        pass