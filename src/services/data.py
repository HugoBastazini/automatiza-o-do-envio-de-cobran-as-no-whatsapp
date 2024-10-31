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
            CREATE TABLE IF NOT EXISTS clientes (
                nome CHAR(40) PRIMARY KEY,
                numero INTEGER NOT NULL,
                telefone INTEGER NOT NULL,
                divida INTEGER NOT NULL
            );
        """)
        
        self.conn.commit()
        print("Banco de dados criado com sucesso.")
        
        self.desconectarBd()
