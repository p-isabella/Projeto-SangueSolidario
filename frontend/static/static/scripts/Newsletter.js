const FormularioNewsletter = document.getElementById('FormularioNewsletter');

const modal = document.querySelector('#staticBackdrop')

FormularioNewsletter.addEventListener('submit', async function(event) {
    event.preventDefault(); // Impede a página de recarregar

    const dadosFormulario = {
    nome: document.getElementById('nome').value,
    email: document.getElementById('email').value
    };

    try {
        const resposta = await fetch('/newsletter', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dadosFormulario)
        })
    
    if (resposta.ok){
        const meuModal = new bootstrap.Modal(modal);
        meuModal.show();
        FormularioNewsletter.reset();
    }

    if (!resposta.ok) {
        alert("Um erro inesperado aconteceu, tente novamente!");
    }
    
    } catch(error){
        console.error('erro de rede', error);
        alert('Sem conexão com o servidor.');
    }
});
