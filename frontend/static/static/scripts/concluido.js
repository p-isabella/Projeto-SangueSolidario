const unidade = JSON.parse(localStorage.getItem('unidadeEscolhida') || 'null');
const agendamento = JSON.parse(sessionStorage.getItem('agendamento') || 'null');

const infoUnidade = document.getElementById('info-unidade');
infoUnidade.textContent = unidade ? unidade.nome : 'Não informada';

const infoData = document.getElementById('info-data');
const infoHora = document.getElementById('info-hora');

if (agendamento && agendamento.data) {
    const [ano, mes, dia] = agendamento.data.split('-');
    infoData.textContent = `${dia}/${mes}/${ano}`;
} else {
    infoData.textContent = 'Não informada';
}

infoHora.textContent = (agendamento && agendamento.hora) || 'Não informado';

document.getElementById('voltar-btn').addEventListener('click', () => {
    localStorage.removeItem('unidadeEscolhida');
    sessionStorage.removeItem('agendamento');
    localStorage.removeItem('selectedDates');
    localStorage.removeItem('selectedTime');
    sessionStorage.removeItem('agendamento');
    window.location.href = '/PaginaInicialUsuario';
});

document.getElementById('voltar-btn').addEventListener('click', () => {
    window.location.href = '/PaginaInicialUsuario';
});
