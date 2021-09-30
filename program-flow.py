name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))

# if age >= 18:
#     print("alright, party on!")
# else:
#     print("you are too young to party!")

if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 18:
    print("just in time to party!")
else:
    print("come on in you old fuck")
