from tkinter import *
from widgets import Widgets

root = Tk()

class Application():
    def __init__(self):
        self.root = root 
        self.Tela()
        root.mainloop()
        widgets = Widgets(root)
    def Tela(self):
        self.root.title("Automação de Mensagens")
        self.root.configure(background="#191970")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=1024, height=768)
        self.root.minsize(width=640, height=480)

Application()