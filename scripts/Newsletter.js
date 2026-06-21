const FormularioNewsletter = document.getElementById('FormularioNewsletter');

FormularioNewsletter.addEventListener('submit', function(event) {
    event.preventDefault(); // Impede a página de recarregar

    const nomeDigitado = document.getElementById('nome').value;
    const emailDigitado = document.getElementById('email').value;

    const dadosNewsletter = {
        nome: nomeDigitado,
        email: emailDigitado
    };

    localStorage.setItem('inscricaoNewsletter', JSON.stringify(dadosNewsletter));

    const modalElement = document.getElementById('staticBackdrop');
    const modal = new bootstrap.Modal(modalElement);
    modal.show(); 

    console.log(dadosNewsletter);
    FormularioNewsletter.reset()

    modalElement.addEventListener('hide.bs.modal', () => {
        if (document.activeElement) {
            document.activeElement.blur();
        }
});
});