numbers = [1, 45, 32, 12, 60]

for number in numbers:
    if number % 8 ==0:
        #reject the list
        print("The numbers are unacceptable, because {} is divisible by 8".format(number))
        break
else: print("All good!")

