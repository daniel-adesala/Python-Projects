"""  
import random
print game art
compare A content
print vs
compare B content
ask user to type A or B according to their answer
if answer is correct convert answer to compare A content
then compare A content with another B content from list of game data contents.
if answer is wrong, end

"""
def compare(x):
    if x == A:
        y = "A"
    else:
        y = "B"
    return f"Compare {y}: {x['name']}, a {x['description']}, from {x['country']}"

import random
from higherlowerart import logo, vs
from higherlowergamedata import data

print(logo)
score = 0

A = data[random.randint(0,49)]

while True:
    
    print(compare(A))
    print(vs)

    while True: 
      B = data[random.randint(0,49)]
      if B != A:
       break

    print(compare(B))

    userchoice = input("Who has more followers? Type 'A' or 'B': ").upper()

    

    if A['follower_count'] > B['follower_count'] and userchoice == 'A':
         score += 1
         print(f"You're right! Current Score: {score}")
        
    elif A['follower_count'] < B['follower_count'] and userchoice == 'B':
         score += 1
         print(f"You're right! Current Score: {score}")
         
         A = B
        
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        print(f"{A['name']} has {A['follower_count']} million followers")
        print(f"{B['name']} has {B['follower_count']} million followers")
        break
    
         
