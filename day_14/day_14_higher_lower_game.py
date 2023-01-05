import random
from day_14_game_data import data
from day_14_art import logo, vs

def choice_1():
    global string_A
    string_A = ""
    choice_A = random.choice(data)
    for key in choice_A:
        if key == "follower_count":
            global follow_count_A
            follow_count_A = choice_A[key]
        if key != "follower_count":
            if key == "country":
                string_A += choice_A[key]
                string_A += "."
            else:
                string_A += choice_A[key]
                string_A += ", "
    return f"Compare A: {string_A}"

def choice_2():
    global string_B
    string_B = ""
    choice_B = random.choice(data) 
    for key in choice_B:
        if key == "follower_count":
            global follow_count_B
            follow_count_B = choice_B[key]
        elif key != "follower_count":
            if key == "country":
                string_B += choice_B[key]
                string_B += "."
            else:
                string_B += choice_B[key]
                string_B += ", "
    return f"Compare B: {string_B}"

def game():

    print(logo)
    score = 0
    running = True
    user_choice_1 = choice_1()
    user_choice_2 = choice_2()
    
    while running:
        
        user_choice_1 = choice_1()
        print(f"Compare A: {string_B}")
        user_choice_2 = choice_2()
        print(vs)
        print(user_choice_2)
    
        user_answer = str(input("Who has more followers? Type 'A' or 'B': ")).capitalize()
            
        if user_answer == "A" and follow_count_A > follow_count_B:
            score += 1
            print(f"You're right! Current score: {score}.")
            
        elif user_answer == "B" and follow_count_B > follow_count_A:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            running = False
            print(f"You're wrong. Your final score is {score}.")
    
game()





