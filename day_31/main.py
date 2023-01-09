from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# UI Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas to create basic view
canvas = Canvas(width=800, height=526)

card_front = PhotoImage(file="day_31/images/card_front.png")
canvas.create_image(400, 263, image=card_front)

title_text = "French"
word_text = "trouve"
canvas.create_text(400, 150, text=title_text, font=('Arial', 40, 'italic'))
canvas.create_text(400, 263, text=word_text, font=('Arial', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="day_31/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, border=0)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="day_31/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, border=0)
wrong_button.grid(column=0, row=1)

window.mainloop()
