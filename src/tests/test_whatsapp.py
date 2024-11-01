import pandas as pd
import sqlite3

class BancoDeDados:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco
        self.conn = None

    def conectar(self):
        """Conecta ao banco de dados SQLite."""
        self.conn = sqlite3.connect(self.nome_banco)

    def desconectar(self):
        """Fecha a conexão com o banco de dados."""
        if self.conn:
            self.conn.close()

    def criar_tabela(self, nome_tabela, colunas):
        """Cria uma tabela no banco de dados se não existir."""
        with self.conn:
            colunas_sql = ', '.join([f"{nome} {tipo}" for nome, tipo in colunas.items()])
            self.conn.execute(f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({colunas_sql})")

    def inserir_dados(self, nome_tabela, dados):
        """Insere dados na tabela."""
        dados.to_sql(nome_tabela, self.conn, if_exists='append', index=False)

def importar_dados_excel(nome_banco, nome_tabela, caminho_arquivo_excel, colunas_tabela):
    banco = BancoDeDados(nome_banco)
    banco.conectar()

    # Cria a nova tabela
    banco.criar_tabela(nome_tabela, colunas_tabela)

    # Limpa a tabela antes de inserir novos dados
    banco.conn.execute(f"DELETE FROM {nome_tabela}")

    # Lê os dados do arquivo Excel
    dados = pd.read_excel(caminho_arquivo_excel)

    # Insere os novos dados na tabela
    banco.inserir_dados(nome_tabela, dados)

    # Fecha a conexão
    banco.desconectar()

# Exemplo de uso
def exemplo():
    caminho_arquivo_excel = 'seu_arquivo.xlsx'  # Altere para o caminho do seu arquivo Excel
    nome_banco_dados = 'seu_banco_de_dados.db'  # Nome do banco de dados SQLite
    nome_nova_tabela = 'nova_tabela'  # Nome da nova tabela que será criada

    # Define a estrutura da nova tabela
    colunas_nova_tabela = {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "coluna1": "TEXT",
        "coluna2": "TEXT",
        "coluna3": "REAL"
    }

    # Chama a função para importar dados do Excel
    importar_dados_excel(nome_banco_dados, nome_nova_tabela, caminho_arquivo_excel, colunas_nova_tabela)

if __name__ == "__main__":
    exemplo()