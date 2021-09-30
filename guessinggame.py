# import math
# from random import seed
# from random import randint
# seed(1)

# answer = randint(1,10)
# print("answer")

answer = 5

print("Please enter a guess between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please guess higher")
    guess = int(input())
elif guess == answer: 
    print("Correct!")
    exit
else: 
    ("Please guess lower")
    guess = int(input()) 

    