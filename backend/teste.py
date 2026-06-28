from CriadorAgendamentos import CriadorAgendamentos
from DoadorConcreto import DoadorConcreto
from AdministradorAgendamentos import AdministradorAgendamentos

# testes pra ver se ta funcionando:
isinha = DoadorConcreto(cpf="123", nome="Isabella", email="isa@email.com", senha="senha123", tipoSanguineo="O-")
joao = DoadorConcreto(cpf="456", nome="Joao", email="joao@email.com", senha="senha456", tipoSanguineo="A+")

fabricaAgendamentos = CriadorAgendamentos()

novoAgendamento = fabricaAgendamentos.criaAgendamentoDoador(oDoador=isinha, data="23/06/2026", hora="08:02", status="pendente", id="1") 

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

#testes do estatico
agendamento1 = fabricaAgendamentos.criaAgendamentoDoador(oDoador=isinha, data="23/06/2026", hora="08:00", status="pendente", id="1")
agendamento2 = fabricaAgendamentos.criaAgendamentoDoador(oDoador=joao, data="23/06/2026", hora="08:00", status="pendente", id="2")  # mesmo horario do 1
agendamento3 = fabricaAgendamentos.criaAgendamentoDoador(oDoador=joao, data="24/06/2026", hora="10:00", status="pendente", id="3")
 
#verifica se nao vai cria outro admin 
print("\nSingleton")
admin1 = AdministradorAgendamentos()
admin2 = AdministradorAgendamentos()
print("admin1 is admin2:", admin1 is admin2)  #True
 
print("\nReservarAgendamento")
print("Status do agendamento1:", agendamento1.PuxaStatus()) #pendente
print("Reservar agendamento1:", admin1.ReservarAgendamento(agendamento1))  #True
print("Status do agendamento1:", agendamento1.PuxaStatus())  #reservado

print("\nverificaDisponibilidade")
#msm horario do 1, nao pode se reservado
print("Disponibilidade do agendamento2:", admin1.verificaDisponibilidade(agendamento2))  #False
print("Tentando reservar agendamento2:", admin1.ReservarAgendamento(agendamento2))  #False
 
print("\nReservar um horario livre")
#dia e hora diferentes do 1, pode reserva
print("Reservar agendamento3:", admin1.ReservarAgendamento(agendamento3))  #True
 
print("\nReagendar")
#antes
print("Agendamento3:", agendamento3.PuxaData(), agendamento3.PuxaHora())
print("Reagendar agendamento3",
      admin1.Reagendar(agendamento3, novaData="23/06/2026", novaHora="09:00"))  #True
#depois
print("Novo agendamento3:", agendamento3.PuxaData(), agendamento3.PuxaHora())

#Tentando reagendar agendamento3 para o msm horario do agendamento1
print("\n",
      admin1.Reagendar(agendamento3, novaData="23/06/2026", novaHora="08:00"))  #False
 
print("\nCancelarAgendamento")
print("Cancelar agendamento1:", admin1.CancelarAgendamento(agendamento1))  #True
print("Status do agendamento1:", agendamento1.PuxaStatus())  #cancelado
print("Cancelar agendamento1 de novo:", admin1.CancelarAgendamento(agendamento1))  #False
