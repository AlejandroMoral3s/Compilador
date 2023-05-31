from tkinter import *

root = Tk()

label1 = Label(root, text='Hola python')
label2 = Label(root, text='Mi nombre es Alejandro')

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

root.mainloop()