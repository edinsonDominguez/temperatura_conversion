from tkinter import Frame, Label, Canvas
from gui import logica
import tkinter.font as tkFont

class Kelvin(Frame):

    def __init__(self, master=None, valor=int, convertir = str):
        super().__init__(master)
        self.master = master
        self.valor = valor
        self.convertir = convertir

        self.config(bg='#585858')

        self.createFrame()

    def createFrame(self):

        fontTitle = tkFont.Font(family="calibri", size=24)
        fontNumber = tkFont.Font(family="arial bold", size=36)
        
        circulo = Canvas(self, width=197, height=180, bg ='#585858')
        circulo.create_oval(190, 5, 5, 175, fill ='#c3c3c3', outline = '#fff')
        circulo.place(x=0, y=70)
        
        lblResultado = Label(self, text = '', bg='#c3c3c3', font=fontNumber, fg='#3f48cc')
          
        if(self.convertir == 'CELSIUS'):
            
            lblResultado.config(text=str(round(logica.kelvin_celsius(self.valor), 1)))
        
        elif(self.convertir == 'FARENHEIT'):
        
            lblResultado.config(text=str(round(logica.temp_kelvin(self.valor), 1)))
            
        
        lblResultado.place(x=20,y=140, width=150, height=50)    
        
        lblSubTitle = Label(self, text='KELVIN', font=fontTitle, fg='#fff', bg ='#585858')
        lblSubTitle.place(x=10, y=330, width=180, height=30)
