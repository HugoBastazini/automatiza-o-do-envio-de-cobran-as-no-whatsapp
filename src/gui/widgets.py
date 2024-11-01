from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
from funcs import Funcs

class Widgets(Funcs):
    def __init__(self, root):
        self.root = root
        self.Frames()
        self.Botoes()
        self.LabelsEntry()
        self.TreeView()
        self.Select()

    def Frames(self):
        self.frame1 = Frame(self.root, bd=2, highlightbackground="black", highlightthickness=2, background="#DCDCDC")
        self.frame1.place(relx=0.01, rely=0.03, relwidth=0.98, relheight=0.64)
        self.frame2 = Frame(self.root, bd=2, highlightbackground="black", highlightthickness=2, background="#DCDCDC")
        self.frame2.place(relx=0.01, rely=0.70, relwidth=0.98, relheight=0.28)

    def Botoes(self):
        self.botaoLimpar = Button(self.frame1, text="LIMPAR", bd=3, bg="#8B0000", fg="white", font=('verdana', 12, 'bold'), command = self.Limpar)
        self.botaoLimpar.place(relx=0.01, rely=0.01, relwidth=0.1, relheight=0.08)
        self.botaoSalvar = Button(self.frame1, text="SALVAR", bd=3, bg="#228B22", fg="white", font=('verdana', 12, 'bold'), command = self.Add)
        self.botaoSalvar.place(relx=0.12, rely=0.01, relwidth=0.1, relheight=0.08)
        self.botaoBuscar = Button(self.frame1, text="BUSCAR", bd=3, font=('verdana', 12, 'bold'))
        self.botaoBuscar.place(relx=0.89, rely=0.01, relwidth=0.1, relheight=0.08)
        self.botaoUpload = Button(self.frame1, text="IMAGEM", command=self.upload_imagem, bd=3, font=('verdana', 12, 'bold'))
        self.botaoUpload.place(relx=0.53, rely=0.01, relwidth=0.1, relheight=0.08)
        self.botaoEnviar = Button(self.frame1, text="ENVIAR", bd=3, font=('verdana', 12, 'bold'))
        self.botaoEnviar.place(relx=0.35, rely=0.77, relwidth=0.1, relheight=0.06)

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
        self.etBusca.place(relx=0.67, rely=0.047, relwidth=0.2)
        self.Logo = Image.open("src/gui/imgs/LOGO X (1).png")
        self.Logo = self.Logo.resize((420,350))
        self.img = ImageTk.PhotoImage(self.Logo)
        self.lbImg = Label(self.frame1, image=self.img, background="#DCDCDC")
        self.lbImg.place(relx=0.6, rely=0.16)
    
    def TreeView(self):

        style = ttk.Style()
        style.theme_use("default")


        style.configure("Treeview.Heading", background="#4682B4", foreground="black", font=("Arial", 10, "bold"))
        
        self.listaClientes = ttk.Treeview(self.frame2, height= 3, column=("col1","col2", "col3", "col4", "col5"))
        self.listaClientes.heading("#0", text="")
        self.listaClientes.heading("#1", text="MENSAGENS")

        self.listaClientes.column('#0', width=0)
        self.listaClientes.column('#1', width=1000)

        self.listaClientes.place(relx=0, rely=0, relwidth=0.98, relheight=1)

        self.scroolLista = Scrollbar(self.frame2, orient='vertical')
        self.listaClientes.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.98, rely=0, relwidth=0.02, relheight=1)