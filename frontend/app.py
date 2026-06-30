from flask import Flask, request, jsonify, render_template, session
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = 'isa'
# PÁGINAS PÚBLICAS (antes de logar)

@app.route('/')
def pagina_inicial():
    return render_template('index.html')

@app.route('/paginaInicial/PossivelDoador')
def possivel_doador():
    return render_template('PossivelDoador.html')

@app.route('/paginaInicial/Cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/paginaInicial/nossasUnidades')
def nossas_unidades():
    return render_template('NossasUnidades.html')

@app.route('/paginaInicial/login')
def login():
    return render_template('login.html')

# ÁREA DO USUÁRIO (logado)

@app.route('/PaginaInicialUsuario')
def pagina_inicial_usuario():
    return render_template('PaginaInicialUsuario.html')

@app.route('/PaginaInicialUsuario/NossasUnidadesUser')
def usuario_unidades():
    return render_template('NossasUnidades.html')

@app.route('/PaginaInicialUsuario/PossivelDoador')
def usuario_possivelDoador():
    return render_template('PossivelDoadorUsuario.html')

@app.route('/usuario/meuPerfil')
def meu_perfil():
    return render_template('meuPerfil.html')

@app.get('/usuario/meuPerfil/ConsultaDados')
def meu_perfil_consulta():
    # AQUI PRECISO DE UMA QUERY DE CONSULTA DOS DADOS DO USUARIO. TODOS OS DADOS!
    return jsonify({
        "nomeCompleto": None,
        "email": None,
        "senha": None
    })

@app.route('/usuario/meuPerfil/EditaDados', methods=['PUT'])
def meu_perfil_edita():
    dados_novos = request.get_json()
    
    nome = dados_novos.get('nomeCompleto')
    email = dados_novos.get('email')
    senha = dados_novos.get('senha')

    # aki vou ter uma edição de usuário em sua classe + essa edição salva no banco de dados
    return jsonify({"status": "sucesso", "mensagem": "Perfil atualizado com sucesso!"}), 200

@app.route('/usuario/meuPerfil/ExcluirConta', methods=['DELETE'])
def meu_perfil_exclui():
    # aqui vou ter a exclusão do usuário no banco de dados via sessão + encerrar a sessão dele
    return jsonify({"status": "sucesso", "mensagem": "Conta excluída com sucesso!"}), 200

@app.route('/usuario/HistoricoAgendamentos')
def historico_agendamentos():
    return render_template('historicoAgendamentos.html')

@app.get('/usuario/HistoricoAgendamentos/consulta')
def historico_agendamentos_consulta():
    # aqi preciso de uma query de consulta do BD E RETORNAR O HISTORICO DO USUARIO!
    return jsonify([])

@app.route('/usuario/HistoricoAgendamentos/excluir/<int:agendamento_id>', methods=['DELETE'])
def historico_agendamentos_excluir(agendamento_id):
    # aqui preciso da exclusão do agendamento (agendamento_id) no banco de dados
    return jsonify({"status": "sucesso", "mensagem": "Agendamento removido com sucesso!"}), 200

# FLUXO DE AGENDAMENTO (usuario logado)
# ordem: local -> calendario -> informacoes -> concluido

@app.route('/usuario/agendamento/local')
def local():
    return render_template('local.html')

@app.route('/usuario/agendamento/unidade', methods=['POST'])
def agendamento_unidade():
    dados = request.get_json()
    return jsonify({"status": "sucesso", "unidade": dados}), 200

@app.route('/usuario/agendamento/calendario')
def calendario():
    return render_template('calendario.html')

@app.route('/usuario/agendamento/informacoes')
def informacoes():
    return render_template('informacoes.html')

@app.route('/agendamento', methods=['POST'])
def criar_agendamento():
    if 'usuario_id' not in session:
        return jsonify({"status": "erro", "mensagem": "Sessão expirada ou usuário não autenticado."}), 401

    dados = request.get_json()
    data = dados.get('data')
    hora = dados.get('hora')
    unidade = dados.get('unidade')
    # tratamento aqui + salvar o agendamento no banco de dados, vinculado ao usuario logado
    return jsonify({"status": "sucesso", "mensagem": "Agendamento criado com sucesso!"}), 201

@app.route('/usuario/agendamento/concluido')
def concluido():
    return render_template('concluido.html')


# AUTENTICAÇÃO

@app.route('/EnvioCadastro', methods=['POST'])
def envio_cadastro():
    dados = request.get_json()

    nome_completo = dados.get('nome_completo')
    cpf = dados.get('cpf')
    tipo_sanguineo = dados.get('tipo_sanguineo')
    data_nascimento = dados.get('data_nascimento')
    cep = dados.get('cep')
    email = dados.get('email')
    senha = dados.get('senha')

    if not email or not senha:
        return jsonify({"status": "erro", "mensagem": "E-mail e senha são obrigatórios!"}), 400

    #!!!! aqui coloca o tratamento + funcoes etc

    return jsonify({"status": "sucesso", "mensagem": "Usuário cadastrado com sucesso!"}), 200

@app.route('/EnvioLogin', methods=['POST'])
def envio_login():
    dados = request.get_json()

    email = dados.get('email')
    senha = dados.get('senha')


    session['usuario_id'] = 11 # usuario de mentira
    # aki trata o login!! valida credenciais no banco + cria sessão/token

    usuario = {
        "nomeCompleto": "Usuário Teste",
        "email": email
    }
    return jsonify({"status": "sucesso", "mensagem": "Usuário logado com sucesso!", "usuario": usuario}), 200

@app.route('/usuario/verificaSessao', methods=['GET'])
def verifica_sessao():
    if 'usuario_id' in session: # faz a verificacao se o usuario ta logado em tudo
        return jsonify({"status": "autenticado", "mensagem": "Sessão ativa"}), 200
    else:
        return jsonify({"status": "nao_autenticado", "mensagem": "Sessão inválida ou expirada."}), 401

@app.route('/Logout', methods=['POST'])
def logout():
    # aki trata o logout!! encerra a sessão/token do usuário
    return jsonify({"status": "sucesso", "mensagem": "Usuário deslogado com sucesso!"}), 200

# NEWSLETTER

@app.route('/newsletter', methods=['POST'])
def cadastrar_newsletter():
    dados = request.get_json()

    nome = dados.get("nome")
    email = dados.get("email")

    if not nome or not email:
        return jsonify({"mensagem": "Nome e e-mail são obrigatórios!"}), 400
    
    return jsonify({"mensagem": "Inscrição realizada com sucesso!"}), 201
    #!!! aqui coloca a instancia com funcao pra salvar no bd e na tabela certa


if __name__ == "__main__":
    app.run(port=3000, debug=True)
