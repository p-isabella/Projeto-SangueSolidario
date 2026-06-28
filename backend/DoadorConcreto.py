from DoadorAbstrato import DoadorAbstrato

class DoadorConcreto(DoadorAbstrato):
    def __init__(self, cpf=None, nome=None, email=None, senha=None, tipoSanguineo=None):
        super().__init__()
        self.__CPF = cpf
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__tipoSanguineo = tipoSanguineo
    
    def ValidaConexaoAgendamentoDoador(self):
        return True
    
    def PuxaCPF(self):
        return self.__CPF

    def PuxaNome(self):
        return self.__nome

    def PuxaSenha(self):
        return self.__senha
    
    def PuxaEmail(self):
        return self.__email
    
    def PuxaTipoSanguineo(self):
        return self.__tipoSanguineo