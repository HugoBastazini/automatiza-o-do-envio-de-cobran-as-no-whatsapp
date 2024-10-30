from tkinter import *

class Widgets():
    def __init__(self, root):
        self.root = root
        self.Frames()

    def Frames(self):
        self.frame1 = Frame(self.root, bd=2, highlightbackground="black", highlightthickness=2)
        self.frame1.place(relx=0.01, rely=0.03, relwidth=0.98, relheight=0.64)
        self.frame2 = Frame(self.root, bd=2, highlightbackground="black", highlightthickness=2)
        self.frame2.place(relx=0.01, rely=0.70, relwidth=0.98, relheight=0.28)

