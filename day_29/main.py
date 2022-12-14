from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbols_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    numbers_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_info = website_entry.get()
    pass_info = password_entry.get()
    email_info = email_entry.get()
    new_data = {
        web_info: {
            "email": email_info,
            "password": pass_info
        }
    }

    if web_info == "" or pass_info == "" or email_info == "":
        messagebox.showinfo(message="You've not entered full information!")
    else:
        messagebox.askokcancel(title=web_info, message=f"You've entered: \nEmail: {email_info}\nPassword: {pass_info}\nIs it okay to save?")
        
        try: 
            with open("day_29/data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        
        except FileNotFoundError:
            with open("day_29/data.json", "w") as data_file:   
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
                
        else:        
            # Updating old data with new data
            data.update(new_data)
            
            with open("day_29/data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")
            
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    web_info = website_entry.get()
    try:
        with open("day_29/data.json") as data_file:
            data = json.load(data_file)
            
            if web_info in data:
                email_info = data[web_info]["email"]
                pass_info = data[web_info]["password"]
                messagebox.showinfo(title=web_info, message=f"Email: {email_info}\nPassword: {pass_info}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {web_info} exists.")
                
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
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
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "smok@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# Buttons
button_generate_password = Button(text="Generate Password", command=generate_pass)
button_generate_password.grid(column=2, row=3)

button_add = Button(text="Add", width=48, command=save)
button_add.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)












window.mainloop()