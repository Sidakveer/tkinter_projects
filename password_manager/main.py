from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


mainWindow = Tk()
mainWindow.title("Password Manager")
mainWindow.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)


website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

website_input = Entry(width=35, bg="white")
website_input.grid(row=1, column=1, columnspan=2)

email_input = Entry(width=35, bg="white")
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=21, bg="white")
password_input.grid(row=3, column=1, sticky="w")

generate_password = Button(text="Generate Password", width=10, highlightthickness=0)
generate_password.grid(row=3, column=2,)

mainWindow.mainloop()