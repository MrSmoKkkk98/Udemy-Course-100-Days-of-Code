import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
game_images = [rock, paper, scissors]
user_choice = int(
    input(f"What do you choose?\nType 0 for rock\n1 for paper\nor 2 for scissors\n"))
if user_choice >= 3:
    print("You typed an invalid number. you lose!")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose: ")
    print(game_images[computer_choice])
if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 0 and computer_choice == 1:
    print("You lose!")
elif user_choice == 0 and computer_choice == 0:
    print("Draw!")

if user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose!")
elif user_choice == 1 and computer_choice == 1:
    print("Draw!")

if user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif user_choice == 2 and computer_choice == 2:
    print("Draw!")



