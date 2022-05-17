from tkinter import Canvas, Frame, Label
from gui import logica
import tkinter.font as tkFont


class Celsius(Frame):

    def __init__(self, master=None, valor=int, convertir = str):
        super().__init__(master)
        self.master = master
        self.valor = valor
        self.convertir = convertir

        self.config(bg='#622524')
        self.createFrame()

    def createFrame(self):
        
        
        fontTitle = tkFont.Font(family="calibri", size=24)
        fontNumber = tkFont.Font(family="arial bold", size=36)
       
        circulo = Canvas(self, width=197, height=180, bg ='#622524')
        circulo.create_oval(190, 5, 5, 175, fill ='#da9695', outline = '#fff')
        circulo.place(x=0, y=70)

        lblResultado = Label(self, text = '', bg='#da9695', font=fontNumber, fg='#3f48cc')
        
        if(self.convertir == 'FARENHEIT'):
            lblResultado.config(text=str(round(logica.temp_celsius_fahr(self.valor), 1)))
            
        elif(self.convertir == 'KELVIN'):           
            lblResultado.config(text=str(round(logica.temp_celsius_kelvin(self.valor), 1)))
        

        lblResultado.place(x=20,y=140, width=150, height=50)

        lblSubTitle = Label(self, text='CELSIUS', font=fontTitle, fg='#fff', bg ='#622524')
        lblSubTitle.place(x=40, y=330, width=100, height=30)


        