low = 1
high = 1000

print("Plz think of number between {} and {} ".format(low, high))
input("Press enter to start")


guesses = 0
guess = 1
while low != high:
   # print("\tGuessing in the range of {} to {}.".format(low, high))
    guess = low + (high - low) // 2 #TODO: Binary checking!
    highLow = input("My guess is {}. Higher, lower, or correct? "
                    "Enter h/l/c:"
                    .format(guess)).casefold()
    if highLow == "h": #Guess higher
        low = guess + 1
    elif highLow == "l":
        high = guess - 1
    else: print("h, l, or c")
    guesses += 1

else:
    print("You thought of the number {}".format(low))
    print("This took me {} guesses".format(guesses))
    

