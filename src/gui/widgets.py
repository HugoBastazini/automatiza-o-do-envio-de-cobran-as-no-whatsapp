from tkinter import *

class Widgets():
    def __init__(self, root):
        self.root = root
        self.Frames()

    def Frames(self):
        self.frame1 = Frame(self.root)
        self.frame1.place(relx=0.01, rely=0.03, relwidth=0.98, relheight=0.5)

