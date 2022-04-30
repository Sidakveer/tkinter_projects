from cgitb import text
from tkinter import *

def update_ans():
    x = input.get()
    km = float(x) * 1.609
    label_ans.config(text=km)


mainWindow = Tk()
mainWindow.title("Mile to Km Converter")
mainWindow.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(row=0, column=1)
input.get()


label = Label(text="Miles")
label.grid(row=0, column=2)

label1 = Label(text="is equal to ")
label1.grid(row=1, column=0,)


label_ans = Label(text="0.0", )
label_ans.grid(row=1, column=1, sticky="nsew")

label2 = Label(text="Km")
label2.grid(row=1, column=2, sticky="nsew")

button = Button(text="Calculate", command=update_ans)
button.grid(row=2, column=1)



mainWindow.mainloop()