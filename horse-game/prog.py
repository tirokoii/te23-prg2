import random
from time import sleep

player_horse = {
    "name": "",
    "speed": 100,
    "agility": 100
}

name_parts = ["ai", "tech", "lord", "evil", "clanker", "pony", "horse", "oat", "datorpony", "poppy", "derek", "speedy", "capitalist", "shower"]

def create_computer_horse():
    speed = random.randint(2, 6)
    name = random.choice(name_parts)
    name_parts.remove(name)
    agility = 8 - speed
    horse = {
        "name": name.capitalize(),
        "speed": speed,
        "agility": agility
    }
    return horse


def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, you can only use numbers")

def input_clamp(stat_name, prompt, clamp = 6):
    while player_horse[stat_name] < 1 or player_horse[stat_name] > clamp:
        player_horse[stat_name] = input_int(prompt)


player_horse['name'] = input("What is your horse name: ").capitalize()

STATS_OK = False

while STATS_OK is False:
    input_clamp("speed", "Whats you horse speed(1-6): ")
    input_clamp("agility", "Whats you horse agility(1-6): ")

    if player_horse["speed"] + player_horse["agility"] == 8:
        STATS_OK = True

computer_horse = create_computer_horse()

print(player_horse)
print(computer_horse)

def game_turn():
    player_speed = player_horse["speed"] = random.randint(1, 6)
    player_agility = random.randint(1, 6) - player_horse["agility"]
    if player_agility >= 0:
        player_speed = player_speed - player_agility
    
    computer_speed = computer_horse["speed"] = random.randint(1, 6)
    computer_agility = random.randint(1, 6) - player_horse["agility"]
    if computer_agility >= 0:
        computer_speed = computer_speed - computer_agility
    
    print(f"Player horse {player_horse['name']} runs {player_speed} in")
    print(f"Player horse {computer_horse['name']} is steps {computer_speed} in")
    return [player_speed, computer_speed]

player_steps = 0
computer_steps = 0

for i in range(1, 11):
    steps = game_turn()
    player_steps += steps[0]
    computer_steps += steps[1]

print(f"Antal steg: {player_horse['name']} {player_steps}, {computer_horse['name']} {computer_steps}")

if player_steps < computer_steps:
    print(f"{computer_horse['name']} won!")
elif player_steps > computer_steps:
    print(f"{player_horse['name']} wins!!!")
else:
    print(f"{player_horse['name']} and {computer_horse['name']} tied!")