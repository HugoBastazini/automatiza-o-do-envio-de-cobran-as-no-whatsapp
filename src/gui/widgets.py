from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

class Widgets():
    def __init__(self, root):
        self.root = root
        self.Frames()
        self.Botoes()
        self.LabelsEntry()
    def Frames(self):
        self.frame1 = Frame(self.root, bd=2, highlightbackground="black", highlightthickness=2, background="#DCDCDC")
        self.frame1.place(relx=0.01, rely=0.03, relwidth=0.98, relheight=0.64)
        self.frame2 = Frame(self.root, bd=2, highlightbackground="black", highlightthickness=2, background="#DCDCDC")
        self.frame2.place(relx=0.01, rely=0.70, relwidth=0.98, relheight=0.28)
    def Botoes(self):
        self.botaoLimpar = Button(self.frame1, text="LIMPAR")
        self.botaoLimpar.place(relx=0.01, rely=0.01, relwidth=0.1, relheight=0.08)
        self.botaoSalvar = Button(self.frame1, text="SALVAR")
        self.botaoSalvar.place(relx=0.12, rely=0.01, relwidth=0.1, relheight=0.08)
        self.botaoBuscar = Button(self.frame1, text="BUSCAR")
        self.botaoBuscar.place(relx=0.89, rely=0.01, relwidth=0.1, relheight=0.08)
        self.botaoUpload = Button(self.frame1, text="IMAGEM", command=self.upload_imagem)
        self.botaoUpload.place(relx=0.53, rely=0.01, relwidth=0.1, relheight=0.08)
    def LabelsEntry(self):
        self.lbMensagem = Label(self.frame1, text="Mensagem", background="#DCDCDC")
        self.lbMensagem.place(relx=0.01, rely=0.13)
        self.txtMensagem = Text(self.frame1)
        self.txtMensagem.place(relx=0.01, rely=0.23, relwidth=0.3, relheight=0.6)
        self.lbLink = Label(self.frame1, text="Link", background="#DCDCDC")
        self.lbLink.place(relx=0.35, rely=0.13)
        self.etLink = Entry(self.frame1)
        self.etLink.place(relx=0.35, rely=0.23, relwidth=0.2)
        self.lbNome = Label(self.frame1, text="Nome", background="#DCDCDC")
        self.lbNome.place(relx=0.35, rely=0.33)
        self.etNome = Entry(self.frame1)
        self.etNome.place(relx=0.35, rely=0.43)
        self.lbData = Label(self.frame1, text="Data", background="#DCDCDC")
        self.lbData.place(relx=0.35, rely=0.53)
        self.etData = Entry(self.frame1)
        self.etData.place(relx=0.35, rely=0.63, relwidth=0.08)
        self.lbTitulo = Label(self.frame1, text="CONSTRUVIDA", background="#DCDCDC", font=("Arial", 20))
        self.lbTitulo.place(relx=0.23, rely=0.003)
        self.etBusca = Entry(self.frame1)
        self.etBusca.place(relx=0.67, rely=0.03, relwidth=0.2)
        self.Logo = Image.open("src/gui/imgs/LOGO X (1).png")
        self.Logo = self.Logo.resize((400,300))
        self.img = ImageTk.PhotoImage(self.Logo)
        self.lbImg = Label(self.frame1, image=self.img, background="#DCDCDC")
        self.lbImg.place(relx=0.64, rely=0.2)
    def upload_imagem(self):
        caminho_imagem = filedialog.askopenfilename(
            title="Selecione uma imagem para upload",
            filetypes=[("Arquivos de imagem", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )