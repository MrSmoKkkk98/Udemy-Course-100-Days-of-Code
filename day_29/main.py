from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_info = website_entry.get()
    pass_info = password_entry.get()
    email_info = email_entry.get()
    
    if web_info != "" or pass_info != "":
        is_ok = messagebox.askokcancel(title=web_info, message=f"You've entered: \nEmail: {email_info}\nPassword: {pass_info}\nIs it okay to save?")
        if is_ok:
            with open("day_29/data.txt", "a") as f:
                f.write(f"{web_info} | {email_info} | {pass_info}\n")
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")
    else:
        messagebox.showinfo(message="You've entered nothing!")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="day_29/logo.png")

canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "smok@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# Buttons
button_generate_password = Button(text="Generate Password")
button_generate_password.grid(column=2, row=3)

button_add = Button(text="Add", width=48, command=save)
button_add.grid(column=1, row=4, columnspan=2)















window.mainloop()