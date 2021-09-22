string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)
print("probably " "pining")
print("Hello " * 5)

today = "friday"
print("day" in today)

#Repfields
Ben = [24, "Ben"]
print ("My age is {0[0]} years and my name is {0[1]}".format(Ben)) #index the tuple

for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3)) #Format size of number

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3)) #Left align

for i in range(1, 13):
    print("No. {0:2} squared is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3)) #center

print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7)) #Floating
print("Pi is approximately {0:12.50f}".format(22/7)) #Precision trumps space
print("Pi is approximately {0:52.50f}".format(22/7)) #Extra space, not enough precision
print("Pi is approximately {0:72.50f}".format(22/7)) 