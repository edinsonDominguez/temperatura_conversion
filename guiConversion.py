from cgitb import text
from heapq import heapify
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


win.mainloop()