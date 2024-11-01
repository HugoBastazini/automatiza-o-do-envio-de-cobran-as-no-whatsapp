import sqlite3

class Bd:
    def conectarBd(self):
        self.conn = sqlite3.connect('clientes.bd')
        self.cursor = self.conn.cursor()
    
    def desconectarBd(self):
        self.conn.close()
    
    def criarBd(self):
        self.conectarBd()
        print("Conectando ao banco de dados...")
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS mensagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mensagem VARCHAR(255) UNIQUE
            );
        """)
        
        self.conn.commit()
        print("Banco de dados criado com sucesso.")
        
        self.desconectarBd()
