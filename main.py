from tkinter import *

FONT_NAME = "Arial"

window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=(FONT_NAME, 10))
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:", font=(FONT_NAME, 10))
username_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=(FONT_NAME, 10))
password_label.grid(row=3, column=0)

generate_password_btn = Button(text="Generate Password")
generate_password_btn.grid(row=3, column=2)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

add_btn = Button(text="Add")
add_btn.config(width=36)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
