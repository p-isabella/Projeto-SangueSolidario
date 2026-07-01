(async function () {
    try {
        const resposta = await fetch('/usuario/verificaSessao', {
            method: 'GET',
            credentials: 'include'
        });
 
        if (!resposta.ok) {
            window.location.href = '/paginaInicial/login';
        }
 
    } catch (erro) {
        console.log('erro ao verificar sessão!', erro);
        window.location.href = '/paginaInicial/login';
    }
})();