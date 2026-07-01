import sqlite3

class databaseAdapter:
  
  def __init__(self):
    self.init_table()
    
  def query(self, query):
    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    print(query)
    cursor.execute(*query)
    resultado = cursor.fetchall()
    connection.commit()
    connection.close()
    return resultado
  
  def init_table(self):
    self.query("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT UNIQUE, senha TEXT)")
    self.query("""CREATE TABLE IF NOT EXISTS agendamentos (id TEXT PRIMARY KEY AUTOINCREMENT, usuario_id INTEGER, data TEXT NOT NULL, hora TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pendente', FOGEIGN KEY (usuario_id) REFERENCES usuarios(id) )""")
    
  """ Queries de Usuário """

  def push_usuario(self, nome, email, senha):
    self.query(["INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?, ?)", (nome, email, senha)])

  def selectBy_usuario(self, id):
    self.query(["SELECT * FROM usuarios WHERE id = ?", (id, )])

  def put_usuario(self, id, nome, email, senha):
    self.query(["UPDATE usuarios SET nome = ?, email = ?, senha = ? WHERE id = ?", (nome, email, senha, id)])

  def delete_usuario(self, id):
    self.query(["DELETE FROM usuarios WHERE id = ?", (id,)])

  """ Queries de Agendamento """

  def push_agendamento(self, id, usuario_id, data, hora, unidade, status):
    self.query(["INSERT INTO agendamentos (id, usuario_id, data, hora, unidade, status) VALUES (?, ?, ?, ?)", (id, usuario_id, data, hora, unidade, status)])

  def selectBy_agendamento(self, id):
    self.query(["SELECT * FROM agendamentos WHERE id = ?", (id, )])

  def delete_agendamento(self, agendamento_id, usuario_id):
    self.query(["DELETE FROM agendamentos WHERE id = ? AND usuario_id = ?", (agendamento_id, usuario_id)])