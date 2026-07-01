document.addEventListener('DOMContentLoaded', async function () {
    const lista = document.getElementById('listaAgendamentos');
    const contador = document.getElementById('contador');
    const modal = document.getElementById('modalExcluir');
    const btnCancelarModal = document.getElementById('btnCancelarModal');
    const btnConfirmarExcluir = document.getElementById('btnConfirmarExcluir');

    let idParaExcluir = null;
    modal.style.display = 'none';

    function abrirModal(id) {
        idParaExcluir = id;
        modal.style.display = 'flex';
        modal.classList.add('aberto');
    }

    function fecharModal() {
        idParaExcluir = null;
        modal.style.display = 'none';
        modal.classList.remove('aberto');
    }

    btnCancelarModal.addEventListener('click', fecharModal);

    btnConfirmarExcluir.addEventListener('click', async function () {
        if (idParaExcluir === null) return;

        try {
            const resposta = await fetch(`/usuario/HistoricoAgendamentos/excluir/${idParaExcluir}`, {
                method: 'DELETE'
            });

            if (resposta.ok) {
                carregarHistorico();
            } else {
                alert('Não foi possível excluir o agendamento.');
            }
        } catch (erro) {
            console.log('erro ao conectar no servidor!', erro);
            alert('Sem conexão com o servidor.');
        } finally {
            fecharModal();
        }
    });

    function renderizarAgendamentos(agendamentos) {
        lista.innerHTML = '';
        contador.textContent = agendamentos.length === 0
            ? 'Nenhum agendamento encontrado.'
            : `${agendamentos.length} agendamento(s) encontrado(s).`;

        agendamentos.forEach(function (agendamento) {
            const item = document.createElement('div');
            item.className = 'item-agendamento';
            item.innerHTML = `
                <div>
                    <strong>${agendamento.unidade || 'Unidade não informada'}</strong><br>
                    📅 ${agendamento.data || '—'} &nbsp; 🕒 ${agendamento.hora || '—'}
                </div>
                <button class="btn-excluir-item" data-id="${agendamento.id}">Excluir</button>
            `;
            lista.appendChild(item);
        });

        document.querySelectorAll('.btn-excluir-item').forEach(function (btn) {
            btn.addEventListener('click', function () {
                abrirModal(this.getAttribute('data-id'));
            });
        });
    }
// requisicao
    async function carregarHistorico() {
        try {
            const resposta = await fetch('/usuario/HistoricoAgendamentos/consulta');
            if (!resposta.ok) {
                throw new Error('Falha ao buscar histórico.');
            }
            const agendamentos = await resposta.json();
            renderizarAgendamentos(agendamentos);
        } catch (erro) {
            console.log('erro ao conectar no servidor!', erro);
            contador.textContent = 'Não foi possível carregar o histórico.';
        }
    }

    carregarHistorico();
});
