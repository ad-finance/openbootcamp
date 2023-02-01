import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=4)

def reiniciar(event):
    selected.set(None)

selected=tkinter.StringVar()

r1=ttk.Radiobutton(window, text='Si', value='1', variable=selected)
r2=ttk.Radiobutton(window, text='No', value='2', variable=selected)
r3=ttk.Radiobutton(window, text='Quizas', value='3', variable=selected)

boton = ttk.Button(window, text = 'Reiniciar')
boton.grid(column=3, row=3, sticky=tkinter.E, padx=5, pady=5)
boton.bind('<Button-1>', reiniciar)

r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)
r3.grid(column=0, row=3, pady=5, padx=5)

window.mainloop()