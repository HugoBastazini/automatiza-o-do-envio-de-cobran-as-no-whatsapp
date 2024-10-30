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
        self.root.configure(background="#FFA617")
        self.root.geometry("1280x720")
        self.root.resizable(True, True)
        self.root.minsize(width=1280, height=720)

Application()