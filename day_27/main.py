from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New Text"

def button_clicked():
    my_label.config(text=input.get())

button = Button(text="Click here", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()
input.get()





















window.mainloop()