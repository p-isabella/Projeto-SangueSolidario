from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# pagina inicial antes de logar:
@app.route('/')
def pagina_inicial():
    return render_template('index.html')

@app.route('/paginaInicial/PossivelDoador')
def possivelDoador():
    return render_template('PossivelDoador.html')

@app.route('/paginaInicial/Cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/paginaInicial/nossasUnidades')
def nossasUnidades():
    return render_template('nossasUnidades.html')

@app.route('/paginaInicial/login')
def login():
    return render_template('login.html')

# usuario!
@app.route('/PaginaInicialUsuario')
def paginaDeUsuario():
    return render_template('PaginaInicialUsuario.html')

@app.route('/usuario/meuPerfil')
def meuPerfil():
    return render_template('meuPerfil.html')

@app.get('/usuario/meuPefil/ConsultaDados')
def meuPefilConsulta():
    return # AQUI PRECISO DE UMA QUERY DE CONSULTA DOS DADOS DO USUARIO. TODOS OS DADOS! 

@app.route('/usuario/meuPefil/EditaDados', methods=['PUT'])
def meuPerfilEdita():
    dadosNovos = request.get_json()
    pass #falta o return
    # aqui vou ter uma edição de usuário em sua classe + essa edição salva no banco de dados
   


@app.route('/usuario/HistoricoAgendamentos')
def HistoricoAgendamentos():
    return render_template('historicoAgendamentos.html')

@app.get('/usuario/HistoricoAgendamentos/consulta')
def historicoAgendamentosConsulta():
    # aqui preciso de uma query de consulta do BD E RETORNAR O HISTORICO DO USUARIO!
    return 

# usuario + agendamento
@app.route('/usuario/agendamento/local')
def local():
    return render_template('local.html')

@app.route('/usuario/usuarioagendamento/informaçoes')
def informacoes():
    return render_template('informacoes.html')

@app.route('/usuario/agendamento/calendario')
def calendario():
    return render_template('calendario.html')

@app.route('/usuario/agendamento/concluido')
def concluido():
    return render_template('concluido.html')

# Dados Newsletter
@app.route('/newsletter', methods=['POST'])
def cadastrarNewsletter():
    dados = request.get_json()

    nome = dados.get("nome")
    email = dados.get("email")

    if not nome or not email:
        return jsonify({"mensagem": "Nome e e-mail são obrigatórios!"}), 400
    
    return jsonify({"mensagem": "Inscrição realizada com sucesso!"}), 201
    #!!! aqui coloca a instancia com funcao pra salvar no bd e na tabela certa

# Dados cadsatro
@app.route('/EnvioCadastro', methods=['POST'])
def EnvioCadastroAoBD():
    dados = request.get_json()

    nome_completo = dados.get('nome_completo')
    cpf = dados.get('cpf')
    tipo_sanguineo = dados.get('tipo_sanguineo')
    data_nascimento = dados.get('data_nascimento')
    cep = dados.get('cep')
    email = dados.get('email')
    senha = dados.get('senha')

    #!!!! aqui coloca o tratamento + funcoes etc

    return jsonify({"status": "sucesso", "mensagem": "Usuário cadastrado com sucesso!"}), 200

# Dados Login
@app.route('/EnvioLogin', methods=['POST'])
def EnvioLogin():
    dados = request.get_json()

    email = dados.get('email')
    senha = dados.get('senha')

    # aki trata o login!!

    return jsonify({"status": "sucesso", "mensagem": "Usuário logado com sucesso!"}), 200



if __name__ == "__main__":
    app.run(port=3000, debug=True)

