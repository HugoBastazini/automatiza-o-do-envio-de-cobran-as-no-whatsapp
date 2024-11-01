from tkinter import *
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from widgets import Widgets
from services.data import Bd

root = Tk()

class Application:
    def __init__(self):
        self.widgets = Widgets(root)
        self.root = root 
        self.banco = Bd()
        self.banco.criarBd() 
        self.Tela()
        root.mainloop()

    def Tela(self):
        self.root.title("Automação de Mensagens")
        self.root.configure(background="#398385")
        root.geometry("1366x768")
        root.minsize(740, 580)

if __name__ == "__main__":
    bd = Bd()
    bd.criarBd()
Application()