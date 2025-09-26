
# class Enemy: #Can't re-use on other enemies
#     def __init__(self): # Self är en 
#         self.hp = 20
#         self.atk = 5
#         self.name =  "Slemper"

#     def print_status(self):
#         print(f"{self.name} is attacking")
#         print(f"hp: {self.hp}")
#         print(f"atk: {self.atk}")

# slime = Enemy()

# slime.print_status()

import random

player = {
    "hp": 20,
    "status": "clear"
}

class Enemy:
    def __init__(self, name: str, HP: int, ATK: int, DEF: int, SPEED: int, skill: list): #Constructor, a method that runs when an instance of a class is called
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.skill = skill
        self.SPEED = SPEED
    
    def attack(self):
        print(f"{self.name.capitalize()} comes charging towards you!")
        print(f"It deals {self.ATK} dmg to the player")
        if player["status"] != False:
            print(f"It inflicts {self.skill[1]}")
        player["hp"] -= self.ATK
        player["status"] = self.skill

    def print_encounter(self):
        print(f"{self.name.capitalize()} is attacking you!")
        print(f"Hp: {self.HP}")

slime1 = Enemy("slime", 7, 3, 2, 2, [{"fire spite": "burnt"}, {"spit": "prazli"}])

slime1.print_encounter()
slime1.attack()

print(player["hp"], player["status"])