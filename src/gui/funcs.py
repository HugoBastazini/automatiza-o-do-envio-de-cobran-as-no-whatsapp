from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.data import Bd

class Funcs(Bd):
    def Limpar(self):
        self.txtMensagem.delete("1.0", END)
        self.etLink.delete(0, END)
        self.etNome.delete(0, END)
        self.etData.delete(0, END)
        self.etBusca.delete(0, END)

    def upload_imagem(self):
        caminho_imagem = filedialog.askopenfilename(
            title="Selecione uma imagem para upload",
            filetypes=[("Arquivos de imagem", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        if caminho_imagem:
            imagem = Image.open(caminho_imagem)
            imagem.thumbnail((100, 100))
            imagem = ImageTk.PhotoImage(imagem)

    def Add(self):
        self.mensagem = self.txtMensagem.get("1.0", END).strip()
        if self.mensagem:
            self.conectarBd()
            self.cursor.execute("""INSERT INTO mensagens (mensagem) 
                VALUES (?)""", (self.mensagem,))
            self.conn.commit()
            self.desconectarBd()
            self.Select()
            self.Limpar()

    def Select(self):
        self.listaClientes.delete(*self.listaClientes.get_children())
        self.conectarBd()
        lista = self.cursor.execute(""" SELECT mensagem FROM mensagens
            ORDER BY mensagem ASC; """)
        for mensagem in lista:
            self.listaClientes.insert("", END, values=mensagem)
        self.desconectarBd()
    
    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label="opções", menu=filemenu)
        menubar.add_cascade(label="Sobre", menu=filemenu2)

        filemenu.add_command(label="Sair", command=Quit)
        filemenu2.add_command(label="Limpa Cliente", command=self.Limpar)
    
    def Buscar(self):
        self.conectarBd()

        self.listaClientes.delete(*self.listaClientes.get_children())

        busca = self.etBusca.get() + "%"

        self.cursor.execute(
            """SELECT mensagem FROM mensagens
            WHERE mensagem LIKE ? ORDER BY mensagem ASC;""",
            (busca,)
        )

        buscaMensagem = self.cursor.fetchall()

        for mensagem in buscaMensagem:
            self.listaClientes.insert("", END, values=mensagem)

        self.etBusca.delete(0, END)

        self.desconectarBd()