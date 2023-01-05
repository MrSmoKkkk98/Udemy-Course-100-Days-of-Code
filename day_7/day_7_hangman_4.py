import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
for char in chosen_word:
    display.append("_")

end_of_game = False
while not end_of_game:
    guess = input("Try to guess a letter. Type your answer here: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
   
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    print(stages[lives])