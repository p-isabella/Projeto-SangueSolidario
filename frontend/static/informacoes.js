const unidade = JSON.parse(localStorage.getItem('unidadeEscolhida') || 'null');
const datas = JSON.parse(localStorage.getItem('selectedDates') || '[]');
const horaSalva = localStorage.getItem('selectedTime');

const params = new URLSearchParams(window.location.search);
const dataParam = params.get('data');
const horaParam = params.get('hora');

const infoUnidade = document.getElementById('info-unidade');
if (unidade) {
    infoUnidade.textContent = unidade.nome;
} else {
    infoUnidade.textContent = 'Não informada';
}

const infoData = document.getElementById('info-data');
const infoHora = document.getElementById('info-hora');

const dataFinal = datas.length > 0 ? datas[0] : dataParam;
const horaFinal = horaSalva || horaParam;

if (dataFinal) {
    const [ano, mes, dia] = dataFinal.split('-');
    infoData.textContent = `${dia}/${mes}/${ano}`;
} else {
    infoData.textContent = 'Não informada';
}

infoHora.textContent = horaFinal || 'Não informado';

document.getElementById('edit-btn').addEventListener('click', () => {
    window.location.href = 'local.html';
});

document.getElementById('confirm-btn').addEventListener('click', () => {
    const btn = document.getElementById('confirm-btn');
    btn.textContent = '✓ Agendamento confirmado!';
    btn.style.backgroundColor = '#27ae60';
    btn.disabled = true;

    setTimeout(() => {
        window.location.href = 'concluido.html';
    }, 2000);
});

document.getElementById('cancel-btn').addEventListener('click', () => {
    const btn = document.getElementById('cancel-btn');

    window.location.href = 'index.html';
});