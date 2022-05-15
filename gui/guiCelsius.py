from tkinter import Frame, Label, Entry, ttk, Button


class Celsius(Frame):

    def __init__(self, master=None, mensaje=str, valor=int):
        super().__init__(master)
        self.master = master
        
        print(mensaje)
        print("valor = ", str(valor))
        self.config(bg='brown')

        self.createFrame()

    def createFrame(self):
        lblSubTitle = Label(self, text='CELSIUS')
        lblSubTitle.place(x=10, y=20, width=100, height=30)