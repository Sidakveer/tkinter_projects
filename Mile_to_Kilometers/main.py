from cgitb import text
from tkinter import *

mainWindow = Tk()
mainWindow.title(text="Mile to Km Converter")

label = Label(text="Miles")
label.grid(row=0, column=2)

label1 = Label(text="is equal to ")
label1.grid(row=1, column=0, sticky="nsew")


label_ans = Label(text=input.get())
label_ans.grid(row=1, column=1, sticky="nsew")


label2 = Label(text="Km")
label2.grid(row=1, column=2, sticky="nsew")

button = Button(text="Calculate")
button.grid(row=2, column=1)

input = Entry()
input.grid(row=0, column=1)

mainWindow.mainloop()