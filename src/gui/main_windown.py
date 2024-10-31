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
        self.root.configure(background="#398385")
        root.geometry("1366x768")
        root.minsize("740","580")


Application()