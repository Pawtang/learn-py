menu = [
    ["egg", "bacon"],
    ["egg", "bacon", "sausage"],
    ["egg", "spam"],
    ["spam", "sausage", "spam", "bacon"],
    ["spam", "spam", "spam", "egg"],
    ["spam", "sausage", "spam", "bacon", "egg"],
    ["spam", "sausage", "spam", "bacon", "sausage"],
]

for meal in menu:
    for index, item in enumerate(meal):
        if item == "spam":
            del meal[index]
    print(meal)

        
    
