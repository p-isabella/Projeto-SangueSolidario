document.addEventListener('DOMContentLoaded', function () {
  let usuario = null;
  try {
    usuario = JSON.parse(localStorage.getItem('usuarioLogado'));
  } catch (erro) {
    usuario = null;
  }

  if (!usuario) {
    window.location.href = '/paginaInicial/login';
    return;
  }

  const inputNome = document.getElementById('perfil_nome');
  const inputEmail = document.getElementById('perfil_email');
  const inputSenha = document.getElementById('perfil_senha');
  const botaoMostrarSenha = document.getElementById('botaoMostrarSenha');

  const areaBotoesPerfil = document.getElementById('areaBotoesPerfil');
  const areaBotoesEdicao = document.getElementById('areaBotoesEdicao');
  const botaoEditarPerfil = document.getElementById('botaoEditarPerfil');
  const botaoExcluirConta = document.getElementById('botaoExcluirConta');
  const botaoSalvarPerfil = document.getElementById('botaoSalvarPerfil');
  const botaoCancelarEdicao = document.getElementById('botaoCancelarEdicao');
  const mensagemDiv = document.getElementById('mensagemPerfil');

  function mostrarMensagem(texto, tipo) {
    mensagemDiv.innerHTML =
      '<div class="alert alert-' + tipo + ' py-2 px-3 d-inline-block">' + texto + '</div>';
  }

  function preencherCampos() {
    inputNome.value = usuario.nomeCompleto || '';
    inputEmail.value = usuario.email || '';
    inputSenha.value = usuario.senha || '';
  }

  preencherCampos();

  botaoMostrarSenha.addEventListener('click', function () {
    const visivel = inputSenha.type === 'text';
    inputSenha.type = visivel ? 'password' : 'text';
    botaoMostrarSenha.textContent = visivel ? 'Mostrar' : 'Ocultar';
  });

  function entrarModoEdicao() {
    inputNome.removeAttribute('readonly');
    inputEmail.removeAttribute('readonly');
    inputSenha.removeAttribute('readonly');
    inputSenha.type = 'text';
    botaoMostrarSenha.disabled = true;

    areaBotoesPerfil.classList.add('d-none');
    areaBotoesEdicao.classList.remove('d-none');
    mensagemDiv.innerHTML = '';
  }

  function sairModoEdicao() {
    inputNome.setAttribute('readonly', true);
    inputEmail.setAttribute('readonly', true);
    inputSenha.setAttribute('readonly', true);
    inputSenha.type = 'password';
    botaoMostrarSenha.disabled = false;
    botaoMostrarSenha.textContent = 'Mostrar';

    areaBotoesPerfil.classList.remove('d-none');
    areaBotoesEdicao.classList.add('d-none');
  }

  botaoEditarPerfil.addEventListener('click', entrarModoEdicao);

  botaoCancelarEdicao.addEventListener('click', function () {
    preencherCampos();
    sairModoEdicao();
    mensagemDiv.innerHTML = '';
  });

  botaoSalvarPerfil.addEventListener('click', function () {
    const novoNome = inputNome.value.trim();
    const novoEmail = inputEmail.value.trim().toLowerCase();
    const novaSenha = inputSenha.value;

    if (!novoNome || !novoEmail || !novaSenha) {
      mostrarMensagem('Preencha nome, e-mail e senha.', 'danger');
      return;
    }

    let usuarios;
    try {
      usuarios = JSON.parse(localStorage.getItem('usuarios')) || [];
    } catch (erro) {
      usuarios = [];
    }

    const emailEmUsoPorOutraConta = usuarios.some(function (u) {
      return u.email === novoEmail && u.cpf !== usuario.cpf;
    });

    if (emailEmUsoPorOutraConta) {
      mostrarMensagem('Esse e-mail já está sendo usado por outra conta.', 'danger');
      return;
    }

    usuarios = usuarios.map(function (u) {
      if (u.cpf === usuario.cpf) {
        return Object.assign({}, u, {
          nomeCompleto: novoNome,
          email: novoEmail,
          senha: novaSenha
        });
      }
      return u;
    });

    try {
      const resposta = await fetch('/usuario/meuPerfil/EditaDados', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          nomeCompleto: novoNome,
          email: novoEmail,
          senha: novaSenha
        })
      });

      if (!resposta.ok) {
        const resultado = await resposta.json();
        mostrarMensagem(resultado.mensagem || 'Erro ao salvar alterações no servidor.', 'danger');
        return;
      }
    } catch (erro) {
      console.log('Erro ao conectar no servidor:', erro);
      mostrarMensagem('Não foi possível salvar no servidor.', 'danger');
      return;
    }

    usuario = Object.assign({}, usuario, {
      nomeCompleto: novoNome,
      email: novoEmail,
      senha: novaSenha
    });
    localStorage.setItem('usuarioLogado', JSON.stringify(usuario));

    preencherCampos();
    sairModoEdicao();
    mostrarMensagem('Dados updated com sucesso!', 'success');
  });

  const botaoHistoricoAgendamentos = document.getElementById('botaoHistoricoAgendamentos');
  botaoHistoricoAgendamentos.addEventListener('click', function () {
    window.location.href = '/usuario/HistoricoAgendamentos';
  });

  botaoExcluirConta.addEventListener('click', function () {
    const confirmar = window.confirm(
      'Tem certeza que deseja excluir sua conta? Essa ação não pode ser desfeita.'
    );
    if (!confirmar) {
      return;
    }

    let usuarios;
    try {
      usuarios = JSON.parse(localStorage.getItem('usuarios')) || [];
    } catch (erro) {
      usuarios = [];
    }

    usuarios = usuarios.filter(function (u) {
      return u.cpf !== usuario.cpf;
    });

    localStorage.setItem('usuarios', JSON.stringify(usuarios));
    localStorage.removeItem('usuarioLogado');

    window.location.href = '/';
  });
});