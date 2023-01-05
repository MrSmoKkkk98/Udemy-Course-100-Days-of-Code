from tkinter import *

def button_clicked():
    my_label.config(text=input.get())
    
window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50,pady=50)

my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.grid(column=0, row=0)

button = Button(text="Click here", command=button_clicked)
button.grid(column=1, row=1)

button_1 = Button(text="New Button", command=button_clicked)
button_1.grid(column=3, row=0)

input = Entry(width=10)
input.grid(column=4, row=2)














window.mainloop()

