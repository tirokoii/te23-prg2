import random
from time import sleep

player_horse = {
    "name": "",
    "speed": 100,
    "agility": 100,
    "steps": 0
}

names = ["Poppy", "Derek", "Speedy", "Capitalist", "Shower"]

# def game_loop(horses):
#     print("------------------------------")
#     for horse in horses:
#         speed = horse["speed"] + random.randint(1,6)
#         agility = horse["agility"] - random.randint(1,6)
#         horse["steps"] += speed + agility
#         print(f"{horse["name"]}: {horse["steps"]}")
#     print("------------------------------")
#     sleep(1)

def game_loop():
    while horses[0]["steps"] < 60 and horses[1]["steps"] < 60 and horses[2]["steps"] < 60 and horses[3]["steps"] < 60:
        print("------------------------------")
        for horse in horses:
            speed = horse["speed"] + random.randint(1,6)
            agility = horse["agility"] - random.randint(1,6)
            horse["steps"] += speed + agility
            print(f"{horse["name"]}: {horse["steps"]}")
        print("------------------------------")
        sleep(1)  
    

def horse():
    total = 8
    name = random.choice(names)
    speed = random.randint(1, 6)
    agility = total - speed
    horse_stats = {
        "name": name,
        "speed": speed,
        "agility": agility,
        "steps": 0
    }
    return horse_stats

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, you can only use numbers")


player_horse['name'] = input("What is your horse name: ")

while player_horse["speed"] + player_horse["agility"] != 8:
    while player_horse["speed"] < 1 or player_horse["speed"] > 6:
        player_horse["speed"] = input_int(f"What is {player_horse['name']}s speed (1-6): ")
    player_horse["agility"] = input_int(f"What is {player_horse['name']}s agility (1-6): ")

horsey_one = horse()
horsey_two = horse()
horsey_three = horse()

horses = [player_horse, horsey_one, horsey_two, horsey_three]

total_laps = 0

# for i in range(1, 7):
#     total_laps += 1
#     print(f"Lap {total_laps}")
#     game_loop(horses)

game_loop()