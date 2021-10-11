menu = [
    ["egg", "bacon"],
    ["egg", "bacon", "sausage"],
    ["egg", "spam"],
    ["spam", "sausage", "spam", "bacon"]
]

for meal in menu:
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item)

    else:
        print(f"{meal} has a spam score of {meal.count('spam')}")