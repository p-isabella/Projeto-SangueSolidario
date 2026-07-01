// requisicao
const formulario = document.querySelector('.formulario')
const aviso = document.querySelector('#Aviso')

formulario.addEventListener('submit', async (evento) => {
    evento.preventDefault()

    const senhaPrincipal = document.querySelector('#criar_senha').value
    const confirmeSenha = document.querySelector('#confirme_senha').value

    if (senhaPrincipal !== confirmeSenha) {
        aviso.innerHTML = `<h1 style="color: red;">As senhas não coincidem!</h1>`;
        return;
    }

    const dadosFormulario = {
        nome_completo: document.querySelector('#nome_completo').value,
        cpf: document.querySelector('#cpf').value,
        tipo_sanguineo: document.querySelector('#tipo_sanguineo').value,
        data_nascimento: document.querySelector('#data_nascimento').value,
        cep: document.querySelector('#cep').value,
        email: document.querySelector('#email').value,
        senha: confirmeSenha
    }

    try {
        const resposta = await fetch('/EnvioCadastro', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dadosFormulario)
        })

        const resultado = await resposta.json().catch(() => ({}))

        if (resposta.ok) {
            aviso.innerHTML = `<h1 style="color: green;">${resultado.mensagem || 'Cadastro realizado com sucesso!'}</h1>`;
            setTimeout(() => {
                window.location.href = '/paginaInicial/login';
            }, 1500);
        } else {
            aviso.innerHTML = `<h1 style="color: red;">${resultado.mensagem || 'Erro ao realizar cadastro.'}</h1>`;
        }

    } catch (error) {
        console.log('erro ao conectar no servidor!', error)
        aviso.innerHTML = `<h1 style="color: red;">Erro ao conectar ao servidor.</h1>`;
    }
})