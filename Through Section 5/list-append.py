parts = ["computer", "monitor", "keyboard", "mouse", "mousepad", "HDMI cable"]

valid_choices = [str(x) for x in range(1, len(parts) + 1)]
print(valid_choices)
choice = '-'
chosen = []

while choice != '0':
    if choice in valid_choices:
        selection = parts[int(choice) - 1]
        print(f"Adding {selection}")
        chosen.append(selection)
        print(f"Current shopping cart: {', '.join(chosen)}")
    else:
        print("Please select an option from the list below: ")
        for i, part in enumerate(parts):
            print(f"{i+1}: {part}")
    choice = input()

