# Car Game
command = ""

while command != "quit":
    command = input("> ").lower()

    if command == "start":
        print("Car started...")
    elif command == "stop":
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
        print("A tow truck is on the way!")
    elif command == "right":
        print("The car has turned to the right")
    elif command == "left":
        print("The car has turned to the left")
    else:
        print("Invalid command")
