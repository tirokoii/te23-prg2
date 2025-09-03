import random
from time import sleep

player_horse = {
    "name": "",
    "speed": 100,
    "agility": 100,
    "steps": 0
}

names = ["Poppy", "Derek", "Speedy", "Capitalist", "Shower", "Flower", "Gifflar", "Spike", "Wrath", "Cookie cream", "Haksholo, of a thousand worlds"]

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
    total_rounds = 0
    while horses[0]["steps"] < 50 and horses[1]["steps"] < 50 and horses[2]["steps"] < 60 and horses[3]["steps"] < 50:
        total_rounds += 1
        print(f"Round {total_rounds}")
        print("------------------------------")
        for horse in horses:
            speed = horse["speed"] + random.randint(1,6)
            agility = horse["agility"] - random.randint(1,6)
            if total_rounds == random.randint(1, 10):
                agility -= random.randint(2, 4)
                print(f"{horse["name"]} slowed down to eat grass!")
            horse["steps"] += speed + agility
            print(f"{horse["name"]}: {horse["steps"]}")
        print("------------------------------")
        sleep(1.5)  
    

def horse():
    total = 8
    name = random.choice(names)
    names.remove(name)
    speed = random.randint(2, 6)
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

horses = [player_horse]

for i in range(1, 4):
    horsey = horse()
    horses.append(horsey)

# total_round = 0

# for i in range(1, 7):
#     total_round += 1
#     print(f"Lap {total_laps}")
#     game_loop(horses)

game_loop()