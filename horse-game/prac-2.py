# total should amount to 30

import random 

horses = [
    {"name": "Thunder", "age": 5, "breed": "Arabian", "color": "Black", "hp": 12, "mp": 10, "sp": 8},
    {"name": "Bella", "age": 7, "breed": "Thoroughbred", "color": "Chestnut", "hp": 10, "mp": 8, "sp": 12},
    {"name": "Storm", "age": 4, "breed": "Quarter Horse", "color": "Gray", "hp": 14, "mp": 6, "sp": 10},
    {"name": "Willow", "age": 6, "breed": "Mustang", "color": "Bay", "hp": 11, "mp": 9, "sp": 10},
    {"name": "Apollo", "age": 8, "breed": "Friesian", "color": "Black", "hp": 15, "mp": 5, "sp": 10},
    {"name": "Daisy", "age": 3, "breed": "Paint Horse", "color": "Pinto", "hp": 9, "mp": 11, "sp": 10}
]

enemy_horses = [
    {"name": "Shadow", "age": 6, "breed": "Morgan", "color": "Dark Bay", "hp": 13, "mp": 7, "sp": 10},
    {"name": "Luna", "age": 5, "breed": "Andalusian", "color": "White", "hp": 10, "mp": 12, "sp": 8},
    {"name": "Blaze", "age": 4, "breed": "Appaloosa", "color": "Spotted", "hp": 11, "mp": 9, "sp": 10},
    {"name": "Athena", "age": 7, "breed": "Clydesdale", "color": "Bay with White Markings", "hp": 16, "mp": 5, "sp": 9},
    {"name": "Zephyr", "age": 3, "breed": "Akhal-Teke", "color": "Golden", "hp": 9, "mp": 11, "sp": 10},
    {"name": "Clover", "age": 8, "breed": "Percheron", "color": "Gray", "hp": 14, "mp": 6, "sp": 10}
]

def horse_info(horse):
    print(f"The fighting horse {horse["name"]} a {horse["age"]} year old {horse["breed"]} with {horse["color"]} fur")

def horse_enemy_roll():
    placement = random.randint(0, 5)
    enemy_horse = enemy_horses[placement]
    return enemy_horse

def turn(player, enemy):
    player_attack = player["mp"] + random.randint(1, 3)
    enemy_attack = enemy["mp"] + random.randint(1, 3)
    if player["sp"] > enemy["sp"]:
        enemy["hp"] -= player_attack
        print(f"The player horse {player["name"]} attacked and dealt {player_attack}")
    elif player["sp"] < enemy["sp"]:
        player["hp"] -= enemy_attack
        print(f"The enemy horse {enemy["name"]} attacked and dealt {enemy_attack}")
    
for horse in horses:
    horse_info(horse)

choice = input("Choose a horse [name]: ")

for horse in horses:
    if choice == horse["name"]:
        player_horse = horse
        break

enemy_horse = horse_enemy_roll()
while player_horse["hp"] > 0 and enemy_horse["hp"] > 0:
    turn(player_horse, enemy_horse)
