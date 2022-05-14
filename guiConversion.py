from tkinter import Tk, Button, Label, Entry, Frame
from gui.guiMenu import Menu

win = Tk()
win.geometry('900x600')
win.resizable(0,0)

contenedor = Frame(win)
contenedor.config(bg = 'blue')
contenedor.place(x=0, y=0, width=900, height=600)


lblTitulo = Label(contenedor, text='CONVERSIONES TERMICAS')
lblTitulo.place(x=300, y=10, width=300, height=30)

menuConversion = Menu(contenedor)
menuConversion.place(x=0, y=50, width=200, height=400)


btn = Button(win, text='selecion')
btn.place(x=300, y=50, width=100, height=30)

contenCelsius = Frame(contenedor)
contenCelsius.config(bg='brown')
contenCelsius.place(x=300, y=80, width=200, height=400) 

contenFahren = Frame(contenedor)
contenFahren.config(bg='gold')
contenFahren.place(x=550, y=80, width=200, height=400) 

contenKelvin = Frame(contenedor)
contenKelvin.config(bg='orangered')
contenKelvin.place(x=300, y=80, width=200, height=400) 

win.mainloop()