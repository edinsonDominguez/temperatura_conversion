import tkinter.font as tkFont
from gui.guiFaren import Faren
from gui.guiCelsius import Celsius
from gui.guiKelvin import Kelvin
from tkinter import  N, W, Frame, Label, Entry, ttk, Button, Tk

def convertir():

    if(combo.get() == 'CELSIUS'):  
        contenFahren = Faren(contenedor, valor=int(txtValor.get()), convertir='CELSIUS')
        contenFahren.place(x=300, y=100, width=200, height=400)

        contenKelvin = Kelvin(contenedor, valor=int(txtValor.get()), convertir='CELSIUS')
        contenKelvin.place(x=550, y=100, width=200, height=400)
 
    elif(combo.get() == 'FARENHEIT'):
        contenCelsius = Celsius(contenedor, valor=int(txtValor.get()), convertir='FARENHEIT')
        contenCelsius.place(x=300, y=100, width=200, height=400)

        contenKelvin = Kelvin(contenedor, valor=int(txtValor.get()), convertir='FARENHEIT')
        contenKelvin.place(x=550, y=100, width=200, height=400)
 
    elif(combo.get() == 'KELVIN'):
        contenCelsius = Celsius(contenedor, valor=int(txtValor.get()), convertir='KELVIN')
        contenCelsius.place(x=300, y=100, width=200, height=400)
        
        contenFahren = Faren(contenedor, valor=int(txtValor.get()), convertir='KELVIN')
        contenFahren.place(x=550, y=100, width=200, height=400)
        
    else:
        print("SELECCIONA LA TEMPERATURA")

win = Tk()
win.geometry('900x600')
win.resizable(0,0)

contenedor = Frame(win)
contenedor.config(bg = '#fff')
contenedor.place(x=0, y=0, width=900, height=600)

fontTitle = tkFont.Font(family="calibri", size=24)
fontText = tkFont.Font(family="calibri", size=16)

lblTitulo = Label(contenedor, text='CONVERSIONES TERMICAS', bg='#9bbb58', fg='#274a50', font=fontTitle)
lblTitulo.place(x=0, y=0, width=900, height=70)

#######################################
menu = Frame(contenedor)
menu.place(x=0, y=70, width=230, height=530)
menu.config(bg='#13de2a')

lblValor = Label(menu, text='Ingresa el valor: ', font=fontText, fg='#274a50', bg='#13de2a', anchor = W)
lblValor.place(x=10, y=10, width=180, height=25)

txtValor = Entry(menu, font=fontText)
txtValor.place(x=10, y=40, width=180, height=27)

lblValor = Label(menu, text='Elige la temperatura ', font=fontText, fg='#274a50', bg='#13de2a', anchor = W)
lblValor.place(x=10, y=70, width=180, height=25)

combo = ttk.Combobox(
menu,
state="readonly",
values=['seleccionar','CELSIUS', 'FARENHEIT', 'KELVIN'],
font=fontText
)

combo.current(0)
combo.place(x=10, y=100, width=180, height=30)

btnConvertir = Button(menu, command= convertir, text="Iniciar", bg='#fdc100', fg='#284b5e', font=fontTitle)
btnConvertir.place(x=40, y=150, width=150, height=40)

##############################################

win.mainloop()