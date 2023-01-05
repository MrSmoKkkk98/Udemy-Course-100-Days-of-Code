import random

word_list = ["aardvark", "baboon", "camel"]
random_item = random.choice(word_list)

guess = input("Try to guess a letter. Type your answer here: ").lower()

for letter in random_item:
    if guess == letter:
        print(f"You've guessed this letter: {guess}")    
    else:
        print(f"You've not guessed the letter.")    
         