from tkinter import Frame, Label, Entry, ttk


class Menu(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.config(bg='red')
        self.crearFrame()

    def crearFrame(self):
        
        lblValor = Label(self, text='Ingresa el valor')
        lblValor.place(x=10, y=10, width=180, height=20)

        txtValor = Entry(self)
        txtValor.place(x=10, y=30, width=100, height=20)

        combo = ttk.Combobox(
            self,
            state="readonly",
            values=['perro', 'gallina', 'pato']
        )
        
        combo.place(x=10, y=60)