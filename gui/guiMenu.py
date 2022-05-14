from msilib.schema import ComboBox
from tkinter import Frame, Label, Entry, ttk, Button


class Menu(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.config(bg='red')
        self.crearFrame()

    def convertir(self):
        print(self.combo.get())
        mensaje = self.combo.get()
        return mensaje

    def crearFrame(self):
        
        lblValor = Label(self, text='Ingresa el valor')
        lblValor.place(x=10, y=10, width=180, height=20)

        txtValor = Entry(self)
        txtValor.place(x=10, y=30, width=100, height=20)

        self.combo = ttk.Combobox(
            self,
            state="readonly",
            values=['seleccionar','CELSIUS', 'FARENHEIT', 'KELVIN']
        )

        self.combo.current(0)
        self.combo.place(x=10, y=60, width=180, height=20)

        btnConvertir = Button(self, command= self.convertir, text="Convertir")
        btnConvertir.place(x=10, y=80, width=100, height=20)
   