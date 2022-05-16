from tkinter import Frame, Label, Entry, ttk, Button
from gui import logica


class Kelvin(Frame):

    def __init__(self, master=None, valor=int, convertir = str):
        super().__init__(master)
        self.master = master
        self.valor = valor
        self.convertir = convertir

        print('Class Kelvin')
        self.config(bg='orangered')

        self.createFrame()

    def createFrame(self):

        lblSubTitle = Label(self, text='KELVIN')
        lblSubTitle.place(x=10, y=20, width=100, height=30)

        lblResultado = Label(self, text = '')
          
        if(self.convertir == 'CELSIUS'):
            
            lblResultado.config(text=str(round(logica.kelvin_celsius(self.valor), 1)))
            lblResultado.place(x=10,y=60, width=100, height=20)
        
        elif(self.convertir == 'FARENHEIT'):
        
            lblResultado.config(text=str(round(logica.temp_kelvin(self.valor), 1)))
            lblResultado.place(x=10,y=60, width=100, height=20)
            
        