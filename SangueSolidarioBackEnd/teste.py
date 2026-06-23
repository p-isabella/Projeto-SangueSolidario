from CriadorAgendamentos import CriadorAgendamentos
from DoadorConcreto import DoadorConcreto

isinha = DoadorConcreto(cpf="123", nome="Isabella", email="isa@email.com", senha="senha123", tipoSanguineo="O-")

fabricaAgendamentos = CriadorAgendamentos()

novoAgendamento = fabricaAgendamentos.criaAgendamentoDoador(oDoador=isinha, data="23/06/2026", hora="08:02", status="linda", id="1") 

# testes pra ver se ta funcionando:

# 1: fabrica de agendamentos
print("hora do agendamento:", novoAgendamento.PuxaHora())
print("id:", novoAgendamento.PuxaID())
print("status do agendamento:", novoAgendamento.PuxaStatus())

print("-"*50)
#mostra quem  eh o doador que ta dentro do agendamentoDoador!
print("teste pra ver se ta dentro:", novoAgendamento.PuxaDoador())

print("-"*50)
# 2: coisas do doadorConcreto isinha
print(isinha.PuxaSenha()) 
print(isinha)
