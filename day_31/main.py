from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# Generate random word
def random_word():
    data_csv = pandas.read_csv("day_31/data/french_words.csv")
    data_csv.to_dict()

    french_words = [word for word in data_csv["French"]]
    eng_words = [word for word in data_csv["English"]]

    rand_index = random.randint(0, len(french_words) - 1)
    rand_french_word = french_words[rand_index]
    global rand_eng_word, flip_timer
    rand_eng_word = eng_words[rand_index]
    window.after_cancel(id=flip_timer)

    french_title = canvas.itemconfig(title_text, text="French", fill="black")
    current_word = canvas.itemconfig(word_text, text=rand_french_word, fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    
    flip_timer = window.after(3000, func=flip_card)

# Flipping the card
def flip_card():
    global rand_eng_word
    eng_title = canvas.itemconfig(title_text, text="English", fill="white")
    current_word = canvas.itemconfig(word_text, text=rand_eng_word, fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

# UI Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Using canvas to create a basic view
canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file="day_31/images/card_front.png")
card_back_img = PhotoImage(file="day_31/images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)

title_text = canvas.create_text(400, 150, text="", font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text="", font=('Arial', 60, 'bold'))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="day_31/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, border=0, command=random_word)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="day_31/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, border=0,  command=random_word)
wrong_button.grid(column=0, row=1)

random_word()

window.mainloop()
