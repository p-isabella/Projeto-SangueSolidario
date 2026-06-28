const formulario = document.querySelector('.formulario')
const aviso = document.querySelector('#Aviso')

formulario.addEventListener('submit', async (evento) => {
    evento.preventDefault()

    const dadosFormulario = {
        nome_completo: document.querySelector('#nome_completo').value,
        cpf: document.querySelector('#cpf').value,
        tipo_sanguineo: document.querySelector('#tipo_sanguineo').value,
        data_nascimento: document.querySelector('#data_nascimento').value,
        cep: document.querySelector('#cep').value,
        email: document.querySelector('#email').value,
        senha: document.querySelector('#confirme_senha').value
    }

    try {
        const resposta = await fetch('http://localhost:3000/EnvioCadastro', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dadosFormulario)
        })


        if (resposta.ok) {
            aviso.innerHTML = `<h1>Cadastro realizado com sucesso!</h1>`;
        } else {
            aviso.innerHTML = `<h1>Erro ao realizar cadastro no servidor.</h1>`;
        }

    } catch(error) {
        console.log('erro ao conectar no servidor!', error)
    }
})