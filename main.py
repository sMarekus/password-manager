from tkinter import *
from tkinter import messagebox

FONT_NAME = "Arial"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(password) == 0 or len(website) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as file:
                file.writelines(f"{website} | {email} | {password}" + "\n")
                file.close()

            website_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
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

website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "john.doe@example.com")

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1, columnspan=1)

add_btn = Button(text="Add", command=save)
add_btn.config(width=43)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
