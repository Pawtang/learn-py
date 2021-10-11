string = "1234;l123afaf465;16;1324;12;341;*;*3;1414"
seperators = ""

for char in string:
    if not char.isnumeric():
        seperators = seperators + char

print(seperators)

