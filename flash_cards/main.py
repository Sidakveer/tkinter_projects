import random
from tkinter import *
import pandas


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
# to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data1 = pandas.read_csv("data/french_words.csv")
    to_learn = data1.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def new_card():
    global timer, current_card
    mainWindow.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    timer = mainWindow.after(3000, card_switch)


def card_switch():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_word, text=current_card["English"], fill="White")


def is_known():
    to_learn.remove(current_card)
    new_card()
    data2 = pandas.DataFrame(to_learn)
    data2.to_csv("data/words_to_learn.csv", index=False)



# UI SETUP
mainWindow = Tk()
mainWindow.title("Flashy")
mainWindow.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = mainWindow.after(3000, card_switch)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

image1 = PhotoImage(file="images/wrong.png")
right_button = Button(image=image1, bg=BACKGROUND_COLOR, highlightthickness=0, command=new_card)
right_button.grid(row=1, column=0)

image2 = PhotoImage(file="images/right.png")
right_button = Button(image=image2, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

new_card()

mainWindow.mainloop()
