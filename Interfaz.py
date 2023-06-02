from tkinter import *

root = Tk()

def desplegar_mensaje():
    label1 = Label(root, text='PUTA')
    label1.pack()

button1 = Button(root, text='PRESIONAME', command=desplegar_mensaje)
button1.pack()

root.mainloop()