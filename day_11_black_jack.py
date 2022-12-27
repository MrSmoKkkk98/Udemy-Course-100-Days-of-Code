import random
from day_11_art import logo

def game():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    blackjack = 21
    user_deck = random.sample(cards, 2)
    computer_deck = random.sample(cards, 2)
    hidden_computer_deck = computer_deck[:-1]
    hidden_computer_deck.append("_")
    print(f"User deck is: {user_deck}")
    print(f"A dealer deck is: {hidden_computer_deck}")

    stand_sum_user_deck = sum(user_deck)
    stand_sum_computer_deck = sum(computer_deck)
    
    going = True
    while going:
        if stand_sum_computer_deck == blackjack:
            print("You've lost. A dealer got a blackjack.")
            going = False
        if stand_sum_user_deck == blackjack:
            print("You've got a blackjack. It's a victory!")
            going = False
        else:    
            user_answer = str(input(f"Do you want to bid on another card or stand yours? Type 'bid' or 'stand': "))

            if user_answer == "bid":
                if sum(user_deck) > 10:
                    for i in range(len(user_deck)):
                        if user_deck[i] == 11:
                            user_deck[i] = 1
                            
                new_card = []
                new_card = random.choice(cards)
                user_deck.append(new_card)
                sum_user_deck = sum(user_deck)
                print(f"\nYour deck after bid: {user_deck}.\n")
                    
                if stand_sum_computer_deck <= 16:
                    new_card = []
                    new_card = random.choice(cards)
                    computer_deck.append(new_card)
                    hidden_computer_deck = computer_deck[:-1]
                    hidden_computer_deck.append("_")
                    print(f"A dealer deck after his bid: {hidden_computer_deck}.\n")
                
                if sum(computer_deck) > 10:
                    for i in range(len(computer_deck)):
                        if computer_deck[i] == 11:
                            computer_deck[i] = 1
                            ace = computer_deck[i]
                    
                if sum(computer_deck) == blackjack or sum_user_deck > blackjack or (sum(computer_deck) > sum_user_deck and sum(computer_deck) <= 21):
                    print(f"You have {user_deck}.\nA dealer has {computer_deck}.\nYou lost!")
                    
                elif sum_user_deck == blackjack or sum(computer_deck) > blackjack or (sum_user_deck > sum(computer_deck) and sum_user_deck <= 21):
                    print(f"You have {user_deck}.\nA dealer has {computer_deck}.\nYou win!")
                
                elif sum(computer_deck) == sum_user_deck:
                    print(f"You have {user_deck}.\nA dealer has {computer_deck}.\nIt's a draw!")
            going = False
                    
            if user_answer == "stand":
                if sum(computer_deck) > 10:
                    for i in range(len(computer_deck)):
                        if computer_deck[i] == 11:
                            computer_deck[i] = 1
                            
                if stand_sum_computer_deck <= 16:
                    new_card = []
                    new_card = random.choice(cards)
                    computer_deck.append(new_card)
                    hidden_computer_deck = computer_deck[:-1]
                    hidden_computer_deck.append("_")
                    print(f"A dealer deck after his bid: {hidden_computer_deck}.\n")
                            
                if stand_sum_computer_deck == blackjack or sum(user_deck) > blackjack or (sum(computer_deck) > stand_sum_user_deck and sum(computer_deck) <= 21):
                    print(f"You have {user_deck}.\nA dealer has {computer_deck}.\nYou lost!")
                    
                elif stand_sum_user_deck == blackjack or sum(computer_deck) > blackjack or (stand_sum_user_deck > sum(computer_deck) and stand_sum_user_deck <= 21):
                    print(f"You have {user_deck}.\nA dealer has {computer_deck}.\nYou win!")
                
                elif sum(computer_deck) == stand_sum_user_deck:
                    print(f"You have {user_deck}.\nA dealer has {computer_deck}.\nIt's a draw!")
            going = False

def restart():    
    restart_game = input("Do you want to play again? If yes press 'y', if no press 'n': ")
    if restart_game == "y":
        game()
    else:
        return 
                
game()
restart()
