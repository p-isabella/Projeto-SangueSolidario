import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FRONTEND_DIR = os.path.dirname(__file__)

for path in [FRONTEND_DIR, ROOT_DIR]:
    if path not in sys.path:
        sys.path.insert(0, path)

from flask import Flask, request, jsonify, render_template, session
from flask_cors import CORS
from databaseAdapter import databaseAdapter
from backend.AdministradorAgendamentos import AdministradorAgendamentos
from backend.AgendamentoDoador import AgendamentoDoador

app = Flask(__name__)
CORS(app)
app.secret_key = 'isa'
# PÁGINAS PÚBLICAS (antes de logar)

database = databaseAdapter()
admin = AdministradorAgendamentos()

def usuario_da_sessao():
    if 'usuario' in session and isinstance(session['usuario'], dict):
        return session['usuario']

    if 'usuario_id' in session:
        return {
            "id": session['usuario_id'],
            "nome_completo": session.get('nome_completo', 'Usuário Teste'),
            "email": session.get('email', ''),
            "senha": session.get('senha', '')
        }

    return None

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
    #consulta de todos os dados---------------------------------------------------------------------------------------------------

    usuario = usuario_da_sessao()
    #qual usuario é esse ---------------------------------------------------------------------------------

    id_usuario = usuario['id']
    database.selectBy_usuario(id_usuario)
    
    if not usuario:
        return jsonify({
            "nome_completo": None,
            "email": None,
            "senha": None
        }), 200

    return jsonify({
        "nome_completo": usuario.get('nome_completo'),
        "email": usuario.get('email'),
        "senha": usuario.get('senha')
    }), 200

@app.route('/usuario/meuPerfil/EditaDados', methods=['PUT'])
def meu_perfil_edita():
    if 'usuario_id' not in session:
        return jsonify({"status": "erro", "mensagem": "Sessão expirada ou usuário não autenticado."}), 401

    dados_novos = request.get_json(silent=True) or {}

    nome = (dados_novos.get('nome_completo') or '').strip()
    email = (dados_novos.get('email') or '').strip().lower()
    senha = (dados_novos.get('senha') or '').strip()

    if not nome or not email or not senha:
        return jsonify({"status": "erro", "mensagem": "Nome, e-mail e senha são obrigatórios."}), 400

    usuario_atual = usuario_da_sessao() or {}
    usuario_atual.update({
        "id": session['usuario_id'],
        "nome_completo": nome,
        "email": email,
        "senha": senha
    })

    session['usuario'] = usuario_atual
    session['nome_completo'] = nome
    session['email'] = email
    session['senha'] = senha

    return jsonify({
        "status": "sucesso",
        "mensagem": "Perfil atualizado com sucesso!",
        "usuario": usuario_atual
    }), 200
    #colocar as edições no banco-------------------------------------------------------------------------------------------

@app.route('/usuario/meuPerfil/ExcluirConta', methods=['DELETE'])
def meu_perfil_exclui():
    if 'usuario_id' in session:
        session.clear()
        return jsonify({"status": "sucesso", "mensagem": "Usuário deletado com sucesso!"}), 200

    return jsonify({"status": "erro", "mensagem": "Nenhuma sessão ativa para encerrar."}), 401

@app.route('/usuario/HistoricoAgendamentos')
def historico_agendamentos():
    return render_template('historicoAgendamentos.html')

@app.get('/usuario/HistoricoAgendamentos/consulta')
def historico_agendamentos_consulta():
    # aqi preciso de uma query de consulta do BD E RETORNAR O HISTORICO DO USUARIO!-----------------------------------------
    return jsonify([])

@app.route('/usuario/HistoricoAgendamentos/excluir/<string:agendamento_id>', methods=['DELETE'])
def historico_agendamentos_excluir(agendamento_id):
    if 'usuario_id' not in session:
        return jsonify({"status": "erro", "mensagem": "Sessão expirada ou usuário não autenticado."}), 401

    agendamento = None
    for item in admin._agendamentos:
        if str(item.PuxaID()) == str(agendamento_id):
            agendamento = item
            break

    if agendamento is None:
        return jsonify({"status": "erro", "mensagem": "Agendamento não encontrado."}), 404

    cancelado = admin.CancelarAgendamento(agendamento)
    if not cancelado:
        return jsonify({"status": "erro", "mensagem": "Não foi possível cancelar o agendamento."}), 400

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

    dados = request.get_json(silent=True) or {}
    data = dados.get('data')
    hora = dados.get('hora')
    unidade = dados.get('unidade')

    if not data or not hora or not unidade:
        return jsonify({"status": "erro", "mensagem": "Dados incompletos do agendamento."}), 400

    agendamento = AgendamentoDoador(
        doador = session['usuario_id'],
        data = data,
        hora = hora,
        status = 'pendente',
        id=f"{session['usuario_id']}-{data}-{hora}"
    )
    agendamento.unidade = unidade

    if not admin.verificaDisponibilidade(agendamento):
        return jsonify({"status": "erro", "mensagem": "Já existe um agendamento para esta data e horário."}), 409

    reservado = admin.ReservarAgendamento(agendamento)
    if not reservado:
        return jsonify({"status": "erro", "mensagem": "Não foi possível reservar o agendamento."}), 409

    database.push_agendamento(
        session['usuario_id'],
        data,
        hora,
        unidade,
        'pendente'
    )

    return jsonify({
        "status": "sucesso",
        "mensagem": "Agendamento criado com sucesso!",
        "agendamento": {
            "id": agendamento.PuxaID(),
            "data": agendamento.PuxaData(),
            "hora": agendamento.PuxaHora(),
            "status": agendamento.PuxaStatus(),
            "unidade": agendamento.unidade
        }
    }), 201

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

    if not email or not senha or not cep or not data_nascimento or not tipo_sanguineo or not cpf or not nome_completo:
        return jsonify({"status": "erro", "mensagem": "Por favor, preencha todos os campos."}), 400

    '''if int(data_nascimento[3:]) < 2010:
        return jsonify({"Você precisa ter no mínimo 16 anos para doar."}), 400'''

    #aqui os dados são enviados para o banco!!!
    database.push_usuario(nome_completo, cpf, tipo_sanguineo, data_nascimento, cep, email, senha)

    return jsonify({"status": "sucesso", "mensagem": "Usuário cadastrado com sucesso!"}), 200

@app.route('/EnvioLogin', methods=['POST'])
def envio_login():
    dados = request.get_json(silent=True) or {}
    email = (dados.get('email') or '').strip().lower()
    senha = (dados.get('senha') or '').strip()

    if not email or not senha:
        return jsonify({"status": "erro", "mensagem": "E-mail e senha são obrigatórios."}), 400

    usuario = database.select_usuario_por_credenciais(email, senha)
    if not usuario:
        return jsonify({"status": "erro", "mensagem": "E-mail ou senha inválidos."}), 401

    usuario = usuario[0]
    usuario_id = usuario[0]
    nome_completo = usuario[1]

    session['usuario_id'] = usuario_id
    session['usuario'] = {
        "id": usuario_id,
        "nome_completo": nome_completo,
        "email": email,
        "senha": senha
    }
    session['nome_completo'] = nome_completo
    session['email'] = email
    session['senha'] = senha

    return jsonify({"status": "sucesso", "mensagem": "Usuário logado com sucesso!", "usuario": session['usuario']}), 200

@app.route('/usuario/verificaSessao', methods=['GET'])
def verifica_sessao():
    if 'usuario_id' in session: # faz a verificacao se o usuario ta logado em tudo
        return jsonify({"status": "autenticado", "mensagem": "Sessão ativa"}), 200
    else:
        return jsonify({"status": "nao_autenticado", "mensagem": "Sessão inválida ou expirada."}), 401

@app.route('/Logout', methods=['POST'])
def logout():
    if 'usuario_id' in session:
        session.clear()
        return jsonify({"status": "sucesso", "mensagem": "Usuário deslogado com sucesso!"}), 200

    return jsonify({"status": "erro", "mensagem": "Nenhuma sessão ativa para encerrar."}), 401

# NEWSLETTER

@app.route('/newsletter', methods=['POST'])
def cadastrar_newsletter():
    dados = request.get_json()

    nome = dados.get("nome")
    email = dados.get("email")

    if not nome or not email:
        return jsonify({"mensagem": "Nome e e-mail são obrigatórios!"}), 400
    
    return jsonify({"mensagem": "Inscrição realizada com sucesso!"}), 201
    # somente perfumaria!

if __name__ == "__main__":
    app.run(port=3000, debug=True)
