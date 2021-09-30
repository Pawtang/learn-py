availableExits = ["north", "south", "east", "west"]

chosenExit = ""
while chosenExit not in availableExits:
    chosenExit = input("Please choose a direction: \n >North \n >South \n >East \n >West \n").casefold()
    if chosenExit == "quit":
        print("Game over")
        break

print("You escaped.")