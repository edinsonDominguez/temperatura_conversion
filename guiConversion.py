from gui.guiCelsius import Celsius
from tkinter import Frame, Label, Entry, ttk, Button, Tk

def convertir():

    if(combo.get() == 'CELSIUS'):
        pass

    elif(combo.get() == 'FARENHEIT'):
        contenCelsius = Celsius(contenedor, combo.get(), valor=int(txtValor.get()))
        contenCelsius.place(x=300, y=80, width=200, height=400)
    
    elif(combo.get() == 'KELVIN'):
        pass
    else:
        print("SELECCIONA LA TEMPERATURA")

win = Tk()
win.geometry('900x600')
win.resizable(0,0)

contenedor = Frame(win)
contenedor.config(bg = 'blue')
contenedor.place(x=0, y=0, width=900, height=600)

lblTitulo = Label(contenedor, text='CONVERSIONES TERMICAS')
lblTitulo.place(x=300, y=10, width=300, height=30)

#######################################
menu = Frame(contenedor)
menu.place(x=0, y=50, width=200, height=400)
menu.config(bg='red')

lblValor = Label(menu, text='Ingresa el valor')
lblValor.place(x=10, y=10, width=180, height=20)

txtValor = Entry(menu)
txtValor.place(x=10, y=30, width=100, height=20)

combo = ttk.Combobox(
menu,
state="readonly",
values=['seleccionar','CELSIUS', 'FARENHEIT', 'KELVIN']
)

combo.current(0)
combo.place(x=10, y=60, width=180, height=20)

btnConvertir = Button(menu, command= convertir, text="Convertir")
btnConvertir.place(x=10, y=80, width=100, height=20)

##############################################

contenFahren = Frame(contenedor)
contenFahren.config(bg='gold')
contenFahren.place(x=550, y=80, width=200, height=400) 

contenKelvin = Frame(contenedor)
contenKelvin.config(bg='orangered')
contenKelvin.place(x=300, y=80, width=200, height=400) 

win.mainloop()