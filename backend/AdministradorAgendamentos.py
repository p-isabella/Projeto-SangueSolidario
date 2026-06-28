class AdministradorAgendamentos:
    _instancia = None

    def __new__(cls):
        #garante so uma instancia
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._agendamentos = []
        return cls._instancia

    def ReservarAgendamento(self, agendamento) -> bool:
        if not self.verificaDisponibilidade(agendamento):
            return False

        agendamento.status = "reservado"
        self._agendamentos.append(agendamento)
        return True

    def CancelarAgendamento(self, agendamento) -> bool:
        for ag in self._agendamentos:
            if ag.PuxaID() == agendamento.PuxaID():
                ag.status = "cancelado"
                self._agendamentos.remove(ag)
                return True
        return False

    def verificaDisponibilidade(self, agendamento) -> bool:
        for ag in self._agendamentos:
            if ag.PuxaData() == agendamento.PuxaData() and ag.PuxaHora() == agendamento.PuxaHora():
                return False  #ja existe agendamento nesse mesmo dia/horario
        return True

    def Reagendar(self, agendamento, novaData=None, novaHora=None) -> bool:
        for ag in self._agendamentos:
            if ag.PuxaID() == agendamento.PuxaID():
                dataAlvo = novaData if novaData is not None else ag.PuxaData()
                horaAlvo = novaHora if novaHora is not None else ag.PuxaHora()

                #verifica se o novo horario nao colide com outro agendamento
                for outro in self._agendamentos:
                    if outro is not ag and outro.PuxaData() == dataAlvo and outro.PuxaHora() == horaAlvo:
                        return False

                ag.data = dataAlvo
                ag.hora = horaAlvo
                return True
        return False