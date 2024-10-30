from tkinter import *
from tkinter import filedialog

class Widgets():
    def __init__(self, root):
        self.root = root
        self.Frames()
        self.Botoes()
        self.LabelsEntry()

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
        self.botaoBuscar.place(relx=0.89, rely=0.01, relwidth=0.1, relheight=0.08)
        self.botaoUpload = Button(self.frame1, text="IMAGEM", command=self.upload_imagem)
        self.botaoUpload.place(relx=0.78, rely=0.01, relwidth=0.1, relheight=0.08)

    def LabelsEntry(self):
        self.lbMensagem = Label(self.frame1, text="Mensagem")
        self.lbMensagem.place(relx=0.01, rely=0.13)
        self.txtMensagem = Text(self.frame1)
        self.txtMensagem.place(relx=0.01, rely=0.23, relwidth=0.3, relheight=0.6)
        self.lbLink = Label(self.frame1, text="Link")
        self.lbLink.place(relx=0.35, rely=0.13)
        self.etLink = Entry(self.frame1)
        self.etLink.place(relx=0.35, rely=0.23)
        self.lbImgAprovada = Label(self.frame1, text="")
        self.lbImgAprovada.place(relx=0.53, rely=0.02)

    def upload_imagem(self):
        caminho_imagem = filedialog.askopenfilename(
            title="Selecione uma imagem para upload",
            filetypes=[("Arquivos de imagem", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        if caminho_imagem:
            self.lbImgAprovada.config(text="Imagem selecionada com sucesso!")