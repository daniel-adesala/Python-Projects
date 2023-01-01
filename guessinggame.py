### intro
### difficulty choice
### Easy level = user has 10 attempts
### Hard level = user has 5 attempts
### declare attempt(s) remaining based on user choice of difficulty
### collect input of user's guess
### state if too high or too low or correct
### if incorrect ask to guess again until attempt gets exhausted or until guess is correct


import random
play_again = 'y'
while play_again == 'y':
    print("Welcome to the number guessing game \nI'm thinking of a number beweeen 1 and 100")

    computer_thought = random.randrange(1, 101)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    while attempts >= 1:
      print(f"You have {attempts} attempts remaining to guess this number")
      user_guess = int(input("Make a guess: "))
      if user_guess == computer_thought:
        print("You're Correct")
        break
      else:
        attempts -= 1
        if user_guess < computer_thought: print("Too Low")
        else: print("Too High")
    else:
        print("You've run out of guesses, You lose")

    play_again = input("Type 'y' to play again, and 'n' to exit: ")
    

