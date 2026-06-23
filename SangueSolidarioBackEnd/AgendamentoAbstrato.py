from abc import ABC, abstractmethod

class AgendamentoAbstrato(ABC):
    @abstractmethod
    def __init__(self, data=None, hora=None, status=None, id=None):
        self.data = data
        self.hora = hora
        self.status = status
        self.id = id
