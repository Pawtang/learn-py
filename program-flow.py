name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))

if age >= 18:
    print("alright, party on!")
else:
    print("you are too young to party!")