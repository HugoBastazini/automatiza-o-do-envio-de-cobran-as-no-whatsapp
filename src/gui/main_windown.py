from tkinter import *
from widgets import Widgets

root = Tk()

class Application():
    def __init__(self):
        self.widgets = Widgets(root)
        self.root = root 
        self.Tela()
        root.mainloop()
    def Tela(self):
        self.root.title("Automação de Mensagens")
        self.root.configure(background="#4682B4")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.root.minsize(width=640, height=480)

Application()