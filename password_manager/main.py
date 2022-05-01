from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for x in range(randint(8, 10))]
    password_symbols = [choice(symbols) for y in range(randint(2, 4))]
    password_numbers = [choice(numbers) for z in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = ''.join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    x = website_input.get()
    y = email_input.get()
    z = password_input.get()

    if len(x) <= 0 or len(y) <= 0 or len(z) <= 0:
        messagebox.showinfo(title="OOPS", message="Please do not leave any field empty")

    else:
        is_ok = messagebox.askokcancel(title=x, message=f"Information entered, \nemail: {y}\npassword: {z}\n"
                                                f"Is it okay to save?")

        if is_ok:
            with open("data.txt", "a", encoding="utf-8") as file1:
                add_str = f"{x} | {y} | {z}\n"
                file1.write(add_str)
                website_input.delete(0, END)
                password_input.delete(0, END)
        else:
            pass




# ---------------------------- UI SETUP ------------------------------- #


mainWindow = Tk()
mainWindow.title("Password Manager")
mainWindow.config(padx=60, pady=60, )

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)


website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "blue_pitch@gmail.com")

password_input = Entry(width=20)
password_input.grid(row=3, column=1)

generate_password = Button(text="Generate Password", width=11, command=gen_pass)
generate_password.grid(row=3, column=2)

add_password = Button(text="Add", width=33, command=save)
add_password.grid(row=4, column=1, columnspan=2)


mainWindow.mainloop()