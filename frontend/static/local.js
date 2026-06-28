let unidadeSelecionada = null;

document.querySelectorAll('.unidade-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
        const imgSrc = this.getAttribute('data-img');
        const label = this.getAttribute('data-label');
        const nomeCompleto = this.textContent.trim();

        const img = document.getElementById('unidade-img');
        const placeholder = document.getElementById('unidade-placeholder');
        const dropdownLabel = document.getElementById('dropdown-label');
        const confirmBtn = document.getElementById('confirm-btn');

        img.src = imgSrc;
        img.classList.remove('d-none');
        placeholder.classList.add('d-none');
        dropdownLabel.textContent = label;

        unidadeSelecionada = {
            label: label,
            nome: nomeCompleto,
            imagem: imgSrc
        };

        confirmBtn.disabled = false;
    });
});

document.getElementById('confirm-btn').addEventListener('click', function() {
    if (!unidadeSelecionada) return;

    localStorage.setItem('unidadeEscolhida', JSON.stringify(unidadeSelecionada));

    this.textContent = '✓ Confirmado!';
    this.style.backgroundColor = '#27ae60';

    setTimeout(() => {
        window.location.href = '/usuario/agendamento/calendario';
    }, 2000);
});