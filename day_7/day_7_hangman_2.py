import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
for char in chosen_word:
    display.append("_")

guess = input("Try to guess a letter. Type your answer here: ").lower()

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if guess == letter:
        display[position] = letter
   