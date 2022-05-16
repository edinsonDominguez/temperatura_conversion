from socket import if_indextoname
from tkinter import Frame, Label
from gui import logica

class Celsius(Frame):

    def __init__(self, master=None, valor=int, convertir = str):
        super().__init__(master)
        self.master = master
        self.valor = valor
        self.convertir = convertir

        print('class Celsius')
        self.config(bg='#622524')
        self.createFrame()

    def createFrame(self):
        
        lblSubTitle = Label(self, text='CELSIUS')
        lblSubTitle.place(x=10, y=20, width=100, height=30)
        
        lblResultado = Label(self, text = '')
        
        if(self.convertir == 'FARENHEIT'):
            print('if:farenheit')
            lblResultado.config(text=str(round(logica.temp_celsius_fahr(self.valor), 1)))
            lblResultado.place(x=10,y=60, width=100, height=20)
 
        elif(self.convertir == 'KELVIN'):
            print('if: Kelvin')
            lblResultado.config(text=str(round(logica.temp_celsius_kelvin(self.valor), 1)))
            lblResultado.place(x=10,y=60, width=100, height=20)
 

        