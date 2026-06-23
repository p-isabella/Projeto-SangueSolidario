from AgendamentoDoador import AgendamentoDoador
from AgendamentoSistema import AgendamentoSistema

class CriadorAgendamentos():
    def criaAgendamentoSistema(self, data, hora, status, id):
        novoAgendamentoSistema = AgendamentoSistema(data=data, hora=hora, status=status, id=id)
        return novoAgendamento

    def criaAgendamentoDoador(self, oDoador, data, hora, status, id):
        novoAgendamentoDoador = AgendamentoDoador(doador=oDoador, data=data, hora=hora, status=status, id=id)
        return novoAgendamentoDoador