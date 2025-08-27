import random

player_horse = {
    "name": "",
    "speed": 1,
    "agility": 1
}

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, you can only use numbers")

player_horse['name'] = input("What is your horse name: ")

while True:
    player_horse['speed'] = input_int(f"What is {player_horse['name']}s speed (1-6): ")
    player_horse['agility'] = input_int(f"What is {player_horse['name']}s agility (1-6): ")

    if int(player_horse['speed']) + int(player_horse['agility']) > 8:
        print("No cheating")
    elif int(player_horse["speed"]) + int(player_horse["agility"]) < 8:
        print("Are you serious")
    else:
        print("Nice")
        break