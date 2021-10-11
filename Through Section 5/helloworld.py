letters = "abcdefghijklmnopqrstuvwxyz"

# backwards = letters[::-1] #backwards slicing idiom
# print(backwards)


print(letters[-10:-13:-1])
print(letters[4::-1])
print(letters[:-9:-1])

# string1 = "he's "
# string2 = "probably "
# string3 = "pining "
# string4 = "for the "
# string5 = "fjords"

# print(string1 + string2 + string3 + string4 + string5)
# print("probably " "pining")
# print("Hello " * 5)

# today = "friday"
# print("day" in today)

# #Repfields
# Ben = [24, "Ben"]
# print ("My age is {0[0]} years and my name is {0[1]}".format(Ben))


#F-strings
name = "Ben"
age = 24
ageInWords = "2 years"
print(name + f" is {age} years old")

print(f"Pi is approximately {22 / 7:12.50f}")