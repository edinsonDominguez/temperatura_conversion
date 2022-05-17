from socket import if_indextoname
from tkinter import Canvas, Frame, Label
from gui import logica

class Celsius(Frame):

    def __init__(self, master=None, valor=int, convertir = str):
        super().__init__(master)
        self.master = master
        self.valor = valor
        self.convertir = convertir

        self.config(bg='#622524')
        self.createFrame()

    def createFrame(self):
        
       
        circulo = Canvas(self, width=200, height=200, bg ='#622524')
        circulo.create_oval(200, 5, 5, 200, fill ='#da9695', outline = '#fff')
        circulo.place(x=0, y=0) 

        lblResultado = Label(self, text = '')
        
        if(self.convertir == 'FARENHEIT'):
            print('if:farenheit')
            lblResultado.config(text=str(round(logica.temp_celsius_fahr(self.valor), 1)))
            lblResultado.place(x=10,y=60, width=100, height=20)
 
        elif(self.convertir == 'KELVIN'):
            print('if: Kelvin')
            lblResultado.config(text=str(round(logica.temp_celsius_kelvin(self.valor), 1)))
            lblResultado.place(x=10,y=60, width=100, height=20)

        lblSubTitle = Label(self, text='CELSIUS')
        lblSubTitle.place(x=10, y=300, width=100, height=30)


        