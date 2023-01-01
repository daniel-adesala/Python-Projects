############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.


import random
import sys


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_choice= input("Do you want to play a game of BlackJack? Type 'y' or 'n' : ")
while user_choice == 'y':
    while True:
        user_cards = random.choices(cards, k=2)
        if 11 in user_cards and sum(user_cards) > 21:
            user_cards.remove(11)
            user_cards.append(1)

        user_current_score = sum(user_cards)
        print(f"Your cards: {user_cards}, current Score: {user_current_score}")
        if user_current_score == 21:
                print("You win, with a Blackjack")
                break
            
        else: 
            computer_card = [random.choice(cards)]
        print(f"Computer's first card: {computer_card}")

        while user_current_score < 21: 
            continue_ = input("Type 'y' to get another card, type 'n' to pass: ")
            if continue_ == 'y' :
              user_cards.append(random.choice(cards))
              user_current_score = sum(user_cards)
              print(f"Your cards: {user_cards}, current Score: {user_current_score}")
            
            
              print(f"Computer's first card: {computer_card}")
            else:
                break

        if user_current_score > 21:          
            print("You went over, you lose")

        else:
            computer_card.extend(random.choices(cards, k = random.randrange(1,3)))
            computer_card_sum = sum(computer_card)
            print(f"Your final hand: {user_cards}, Your final score: {user_current_score} \nComputer's final hand: {computer_card}, Computer's final score: {sum(computer_card)} ")
            
            if user_current_score == 21:
                print("You win, with a Blackjack")
            elif user_current_score > computer_card_sum or  21 < computer_card_sum :
               print("You win")
            elif user_current_score == computer_card_sum:
                print("It's a draw!!")
            elif computer_card_sum == 21:
                print("You lose, Opponent has Blackjack")
            else:
              print("You lose")
            break
    print()
    user_choice = input ("Do you want to play again? type 'y' or 'n': ")
    print()