from tkinter import Tk, Button, Label, Entry, Frame
from turtle import bgcolor

win = Tk()
win.geometry('900x600')
win.resizable(0,0)

contenedor = Frame(win)
contenedor.config(bg = 'blue')
contenedor.place(x=0, y=0, width=900, height=600)



win.mainloop()