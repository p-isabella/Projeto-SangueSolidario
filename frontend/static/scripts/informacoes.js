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

document.getElementById('edit-btn').addEventListener('click', () => {
    window.location.href = '/usuario/agendamento/calendario';
});


// requisicao
document.getElementById('confirm-btn').addEventListener('click', async () => {
    const btn = document.getElementById('confirm-btn');

    if (!unidade || !agendamento) {
        alert('Faltam dados do agendamento. Por favor, refaça o processo.');
        return;
    }

    try {
        const resposta = await fetch('/agendamento', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                data: agendamento.data,
                hora: agendamento.hora,
                unidade: unidade.nome 
            })
        });

        if (resposta.ok) {
            btn.textContent = '✓ Agendamento confirmado!';
            btn.style.backgroundColor = '#27ae60';
            btn.disabled = true;

            setTimeout(() => {
                window.location.href = '/usuario/agendamento/concluido';
            }, 1500);
        } else {
            alert('Erro ao confirmar agendamento no servidor.');
        }
    } catch (error) {
        console.log('erro ao conectar no servidor!', error);
        alert('Sem conexão com o servidor.');
    }
});