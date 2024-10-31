from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

class Funcs():
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