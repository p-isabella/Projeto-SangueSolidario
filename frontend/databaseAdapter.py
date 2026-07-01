import sqlite3

class databaseAdapter:
  
  def __init__(self):
    self.init_table()
    
  def query(self, sql, params=None):
    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    print(sql)
    if params is not None:
      print("entrou no params")
      cursor.execute(sql, params)
    else:
      print("não entrou no params")
      cursor.execute(sql)
    resultado = cursor.fetchall()
    connection.commit()
    connection.close()
    return resultado
  
  def init_table(self):
    self.query("CREATE TABLE IF NOT EXISTS usuarios (usuario_id INTEGER PRIMARY KEY AUTOINCREMENT, nome_completo TEXT, cpf TEXT UNIQUE, tipo_sanguineo TEXT, data_nascimento TEXT, cep TEXT, email TEXT UNIQUE, senha TEXT)")
    self.query("""CREATE TABLE IF NOT EXISTS agendamentos (
      agendamento_id INTEGER PRIMARY KEY AUTOINCREMENT,
      usuario_id INTEGER NOT NULL,
      data TEXT NOT NULL,
      hora TEXT NOT NULL,
      unidade TEXT,
      status TEXT NOT NULL DEFAULT 'pendente',
      FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
    )""")
    
  """ Queries de Usuário """

  def push_usuario(self, nome_completo, cpf, tipo_sanguineo, data_nascimento, cep,  email, senha):
    self.query(
      "INSERT INTO usuarios (nome_completo, cpf, tipo_sanguineo, data_nascimento, cep, email, senha) VALUES (?, ?, ?, ?, ?, ?, ?)",
      (nome_completo, cpf, tipo_sanguineo, data_nascimento, cep, email, senha)
    )

  def selectBy_usuario(self, usuario_id):
    return self.query(
      "SELECT * FROM usuarios WHERE usuario_id = ?",
      (usuario_id, )
    )
    # return usuario??? como faz

  def select_usuario_por_credenciais(self, email, senha):
    return self.query(
      "SELECT usuario_id, nome_completo, cpf, tipo_sanguineo, data_nascimento, cep, email, senha FROM usuarios WHERE email = ? AND senha = ?",
      (email, senha)
    )

  def put_usuario(self, usuario_id, nome, email, senha):
    self.query(
      "UPDATE usuarios SET nome_completo = ?, email = ?, senha = ? WHERE usuario_id = ?",
      (nome, email, senha, usuario_id)
    )

  def delete_usuario(self, usuario_id):
    self.query(
      "DELETE FROM usuarios WHERE usuario_id = ?",
      (usuario_id, )
    )

  """ Queries de Agendamento """

  def push_agendamento(self, usuario_id, data, hora, unidade, status):
    self.query(
      "INSERT INTO agendamentos (usuario_id, data, hora, unidade, status) VALUES (?, ?, ?, ?, ?)",
      (usuario_id, data, hora, unidade, status)
    )

  def selectBy_agendamento(self, usuario_id):
    return self.query(
      "SELECT * FROM agendamentos WHERE usuario_id = ?",
      (usuario_id, )
    )

  def delete_agendamento(self, agendamento_id, usuario_id):
    self.query(
      "DELETE FROM agendamentos WHERE agendamento_id = ? AND usuario_id = ?",
      (agendamento_id, usuario_id)
    )
