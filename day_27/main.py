from tkinter import *

def miles_to_km():
    miles = input.get()
    km = float(miles) * 1.689
    km_result.config(text=round(km, 2))

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

miles = Label(text="Miles", font=("Arial", 12), justify="left")
miles.grid(column=3, row=1)

kilometers = Label(text="Kilometers", font=("Arial", 12), justify="center")
kilometers.grid(column=3, row=2)

km_result = Label(text="0", font=("Arial", 12), justify="center")
km_result.grid(column=2, row=2)

is_equal_to = Label(text="is equal to", font=("Arial", 12), justify="right")
is_equal_to.grid(column=1, row=2)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=3)

input = Entry(width=10, justify="left")
input.grid(column=2, row=1)










window.mainloop()

