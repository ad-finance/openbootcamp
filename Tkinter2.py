import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

seleccionado=tkinter.StringVar

checkbox1 = ttk.Checkbutton(window, text='checkbox1', variable=seleccionado)
checkbox1.grid(row=0,column=0)

checkbox2 = ttk.Checkbutton(window, text='checkbox2', variable=seleccionado)
checkbox2.grid(row=1,column=0)

checkbox3 = ttk.Checkbutton(window, text='checkbox3', variable=seleccionado)
checkbox3.grid(row=2,column=0)

Label1 = ttk.Label(window, text='Label1', background="blue", foreground="green")
Label1.grid(row=3, column=0, padx=5, pady=5)

window.mainloop()
