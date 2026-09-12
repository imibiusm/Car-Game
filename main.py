# Car Game
command = ""
started = False
is_towed = False
while command != "quit":
    command = input("> ").lower()

    if command == "start":
        if started:
            print("The car is already started...")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("The car is already stopped!")
        else:
            started = False
            print("Car stopped...")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
right - to turn the car right
left - to turn the car left
tow - to tow the car
""")
    elif command == "quit":
        print("Game ended.")
    elif command == "tow":
        if is_towed:
            print("Your car is already towed!")
        if started == True:
            print("The car is already started you can not tow it!")
        else:
            towed = True
            print("Towing")
    elif command == "right":
        print("The car has turned to the right")
    elif command == "left":
        print("The car has turned to the left")
    else:
        print("Invalid command")
