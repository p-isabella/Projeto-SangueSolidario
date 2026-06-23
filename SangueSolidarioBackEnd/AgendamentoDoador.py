from AgendamentoAbstrato import AgendamentoAbstrato
from DoadorAbstrato import DoadorAbstrato

class AgendamentoDoador(AgendamentoAbstrato):
    def __init__(self, doador=None, data=None, hora=None, status=None, id=None):
        super().__init__(data, hora, status, id)
        self.doador = doador
    
    def PuxaDoador(self):
        return self.doador

    def PuxaData(self):
        return self.data

    def PuxaHora(self):
        return self.hora

    def PuxaStatus(self):
        return self.status
        
    def PuxaID(self):
        return self.id