const formularioLogin = document.querySelector('.formulario')
const aviso = document.querySelector('#Aviso')

formularioLogin.addEventListener('submit', async (evento) => {
    evento.preventDefault()

    const dadosLogin = {
        email: document.querySelector('#email').value,
        senha: document.querySelector('#entrar_senha').value
    }

    try {
        const resposta = await fetch('http://localhost:3000/EnvioLogin', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dadosLogin)
        })

        if (resposta.ok) {
            aviso.innerHTML = `<h1>Login realizado com sucesso!</h1>`;
            setTimeout(() => {
                window.location.href = '/PaginaInicialUsuario';
            }, 1500);
        } else {
            aviso.innerHTML = `<h1>Erro ao realizar login no servidor.</h1>`;
        }

    } catch (error) {
        console.log('erro ao conectar no servidor!', error)
    }
})