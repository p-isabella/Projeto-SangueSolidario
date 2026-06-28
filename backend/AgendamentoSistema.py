from AgendamentoAbstrato import AgendamentoAbstrato

class AgendamentoSistema(AgendamentoAbstrato):
    def __init__(self, data=None, hora=None, status=None, id=None):
        super().__init__(self, data, hora, status=None, id=None)
        
    def PuxaData(self):
        return self.data

    def PuxaHora(self):
        return self.hora

    def PuxaStatus(self):
        return self.status

    def PuxaID(self):
        return self.id