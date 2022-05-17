from cgitb import text
from tkinter import *


win = Tk()
win.geometry('600x600')
lbl = Label(text = 'Hola mundo')
lbl.pack()

circulo = Canvas(width=200, height=200, bg='blue')
circulo.create_oval(200, 5, 5, 200)
circulo.pack()

win.mainloop()