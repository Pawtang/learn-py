str = input("3 nums comma separated: ")
ints = str.split(', ')
integers = []
for x in ints:
    integers.append(int(x))
    

print(integers[0] + integers[1] - integers[2])