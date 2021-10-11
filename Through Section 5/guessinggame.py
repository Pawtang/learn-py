import math
import random

low = 1
high = 20
answer = random.randint(low, high)
print(answer) # TODO: Remove after testing

print("Please enter a guess between {} and {}: ".format(low, high))

guess = int(input())
while guess != answer:
    if guess == 0:
        print("OK, game over!")
        break
    elif guess == answer:
     print("correct!")
     break
    elif guess < answer:
        print("Please guess higher")
        guess = int(input())
    elif guess not in range (low, high):
        print(f"Please enter a guess between {low} and {high}: ")
        guess = int(input())
    else: 
        print("Please guess lower")
        guess = int(input())
else: print("You got ")
    
