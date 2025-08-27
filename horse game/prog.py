import random

player_horse = {
    "name": "",
    "speed": 100,
    "agility": 100
}

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, you can only use numbers")

speed = player_horse['speed']
agility = player_horse['agility']
name = player_horse['name']

player_horse['name'] = input("What is your horse name: ")

while speed + agility != 8:
    while speed < 1 or agility > 6:
        speed = input_int(f"What is {name}s speed (1-6): ")
    agility = input_int(f"What is {name}s agility (1-6): ")
