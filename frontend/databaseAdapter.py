import sqlite3

class databaseAdapter:
  
  def __init__(self):
    self.init_table()
    
  def query(self, query, params=None):
    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    print(query)
    if params:
      cursor.execute(query,params)
    else:
      cursor.execute(query)
    resultado = cursor.fetchall()
    connection.commit()
    connection.close()
    return resultado
  
  def init_table(self):
    self.query("CREATE TABLE IF NOT EXISTS usuarios (usuario_id INTEGER PRIMARY KEY AUTOINCREMENT, nome_completo TEXT, cpf TEXT UNIQUE, tipo_sanguineo TEXT, data_nascimento TEXT, cep TEXT, email TEXT UNIQUE, senha TEXT)")
    self.query("""CREATE TABLE IF NOT EXISTS agendamentos (usuario_id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT NOT NULL, hora TEXT NOT NULL, unidade TEXT, status TEXT NOT NULL DEFAULT 'pendente', FOREIGN KEY (usuario_id) REFERENCES usuarios(id) )""")
    
  """ Queries de Usuário """

  def push_usuario(self, nome_completo, cpf, tipo_sanguineo, data_nascimento, cep,  email, senha):
    self.query(["INSERT INTO usuarios (nome_completo, cpf, tipo_sanguineo, data_nascimento, cep, email, senha) VALUES (?, ?, ?, ?, ?, ?, ?)", (nome_completo, cpf, tipo_sanguineo, data_nascimento, cep, email, senha)])

  def selectBy_usuario(self, id):
    return self.query(["SELECT * FROM usuarios WHERE id = ?", (id, )])

  def put_usuario(self, id, nome, email, senha):
    self.query(["UPDATE usuarios SET nome_completo = ?, email = ?, senha = ? WHERE id = ?", (nome, email, senha, id)])

  def delete_usuario(self, id):
    self.query(["DELETE FROM usuarios WHERE id = ?", (id, )])

  """ Queries de Agendamento """

  def push_agendamento(self, usuario_id, data, hora, unidade, status):
    self.query(["INSERT INTO agendamentos (usuario_id, data, hora, unidade, status) VALUES (?, ?, ?, ?)", (id, usuario_id, data, hora, unidade, status)])

  def selectBy_agendamento(self, id):
    self.query(["SELECT * FROM agendamentos WHERE id = ?", (id, )])

  def delete_agendamento(self, agendamento_id, usuario_id):
    self.query(["DELETE FROM agendamentos WHERE id = ? AND usuario_id = ?", (agendamento_id, usuario_id)])
