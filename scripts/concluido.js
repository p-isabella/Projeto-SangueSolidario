const unidade = JSON.parse(localStorage.getItem('unidadeEscolhida') || 'null');
const datas = JSON.parse(localStorage.getItem('selectedDates') || '[]');
const horaSalva = localStorage.getItem('selectedTime');

const infoUnidade = document.getElementById('info-unidade');
if (unidade) {
    infoUnidade.textContent = unidade.nome;
} else {
    infoUnidade.textContent = 'Não informada';
}

const infoData = document.getElementById('info-data');
const infoHora = document.getElementById('info-hora');

if (datas.length > 0) {
    const [ano, mes, dia] = datas[0].split('-');
    infoData.textContent = `${dia}/${mes}/${ano}`;
} else {
    infoData.textContent = 'Não informada';
}

infoHora.textContent = horaSalva || 'Não informado';

document.getElementById('voltar-btn').addEventListener('click', () => {
    localStorage.removeItem('unidadeEscolhida');
    localStorage.removeItem('selectedDates');
    localStorage.removeItem('selectedTime');
    window.location.href = 'index.html';
});