import random
from day_12_art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': "))

def asking_user():
    global user_guess
    user_guess = int(input("Guess a number between 1 and 100. Type number here: "))
 
answer = random.randint(1, 100)
hard_turns = 5
easy_turns = 10
running = True
while running:
    if (hard_turns > 0 and hard_turns < 6 and difficulty == "hard") or (easy_turns > 0 and easy_turns < 11 and difficulty == "easy"):
        easy_turns -= 1
        hard_turns -= 1
        asking_user()
        if easy_turns == 0 or hard_turns == 0:
            print("You've lost all your turns.")
           
        if answer == user_guess:
            print(f"You're guessed a number {answer}. Well done!")
            running = False
            
        elif answer > user_guess:
            print("Too low")
        
        elif answer < user_guess:
            print("Too high")
        
            
       