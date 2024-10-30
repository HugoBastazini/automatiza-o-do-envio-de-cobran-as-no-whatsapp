from tkinter import *

class Widgets():
    def __init__(self, root):
        self.root = root
        self.Frames()
        self.Botoes()
    def Frames(self):
        self.frame1 = Frame(self.root, bd=2, highlightbackground="black", highlightthickness=2)
        self.frame1.place(relx=0.01, rely=0.03, relwidth=0.98, relheight=0.64)
        self.frame2 = Frame(self.root, bd=2, highlightbackground="black", highlightthickness=2)
        self.frame2.place(relx=0.01, rely=0.70, relwidth=0.98, relheight=0.28)
    def Botoes(self):
        self.botaoLimpar = Button(self.frame1, text="LIMPAR")
        self.botaoLimpar.place(relx=0.01, rely=0.01, relwidth=0.1, relheight=0.08)
        self.botaoSalvar = Button(self.frame1, text="SALVAR")
        self.botaoSalvar.place(relx=0.12, rely=0.01, relwidth=0.1, relheight=0.08)
        self.botaoBuscar = Button(self.frame1, text="BUSCAR")
        self.botaoBuscar.place(relx=0.23, rely=0.01, relwidth=0.1, relheight=0.08)

