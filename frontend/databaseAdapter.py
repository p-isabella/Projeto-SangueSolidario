import sqlite3

class databaseAdapter:
  
  def __init__(self):
    self.init_table()
    
  def init_table(self):
    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT UNIQUE, senha TEXT)")
    connection.commit()
    connection.close()
    
  def query(self, query):
    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    cursor.execute(*query)
    connection.commit()
    connection.close()