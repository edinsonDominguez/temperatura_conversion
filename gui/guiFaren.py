from tkinter import Frame, Label, Entry, ttk, Button
from gui import logica

class Faren(Frame):

    def __init__(self, master=None, valor=int, convertir = str):
        super().__init__(master)
        self.master = master
        self.valor = valor
        self.convertir = convertir

        print('class Faren')
        self.config(bg='gold')
        self.createFrame()

    def createFrame(self):
        
        lblSubTitle = Label(self, text='FAHRENHEIT')
        lblSubTitle.place(x=10, y=20, width=100, height=30)
        lblResultado = Label(self, text = '')
        

        if(self.convertir == 'CELSIUS'):

            lblResultado.config(text=str(round(logica.temp_fahrenheit(self.valor), 1)))
            lblResultado.place(x=10,y=60, width=100, height=20)
        
        elif(self.convertir == 'KELVIN'):
            
            lblResultado.config(text=str(round(logica.kelvin_faren(self.valor), 1)))
            lblResultado.place(x=10,y=60, width=100, height=20)
        