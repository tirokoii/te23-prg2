
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

# player = {
#     "hp": 20,
#     "status": "clear"
# }

# class Enemy:
#     def __init__(self, name: str, HP: int, ATK: int, DEF: int, SPEED: int, skill: list): # Constructor, a method that runs when an instance of a class is called
#         self.name = name
#         self.HP = HP
#         self.ATK = ATK
#         self.DEF = DEF
#         self.skill = skill
#         self.SPEED = SPEED
    
#     def attack(self):
#         print(f"{self.name.capitalize()} comes charging towards you!")
#         print(f"It deals {self.ATK} dmg to the player")
#         if player["status"] != False:
#             print(f"It inflicts {self.skill[1]}")
#         player["hp"] -= self.ATK
#         player["status"] = self.skill[1]

#     def print_encounter(self):
#         print(f"{self.name.capitalize()} is attacking you!")
#         print(f"Hp: {self.HP}")


# slime1 = Enemy("slime", 7, 3, 2, 2, [{"fire spite": "burnt"}, {"spit": "prazli"}]) # Instance

# slime1.print_encounter()
# slime1.attack()

# print(player["hp"], player["status"])


# class Enemy:
#     def __init__(self, name: str, HP: int, ATK: int, DEF: int, SPEED: int, skill: list): # Constructor, a method that runs when an instance of a class is called
#         self.name = name
#         self.HP = HP
#         self.ATK = ATK
#         self.DEF = DEF
#         self.skill = skill
#         self.SPEED = SPEED
    
#     def check_for_death(self):
#         if self.HP <= 0:
#             print("Dead")
#             return False

#     def attack(self):
#         print(f"{self.name.capitalize()} comes charging towards you!")
#         return self.ATK

#     def print_encounter(self):
#         print(f"{self.name.capitalize()} is attacking you!")
#         return self.HP
    
# def attack(enemy_one, enemy_two):
#     enemy_one.print_encounter()
#     enemy_one.attack()
#     print(f"It deals {enemy_one.ATK} dmg to the {enemy_two.name}")
#     enemy_two.HP =- enemy_one.ATK

# slime = Enemy("Slime", 10, 4, 1, {"Prazil": "Pras"}, 2)
# goblin = Enemy("Goblin", 15, 5, 0, {"Killswitch": "bam"}, 4)

# attack(slime, goblin)

board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
    ]

class Enemy:
    def __init__(self, name: str, HP: int, ATK: int, DEF: int, skill: dict, SPEED: int, y: int, x: int, side: str, RANGE: int): # Constructor, a method that runs when an instance of a class is called
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.skill = skill
        self.SPEED = SPEED
        self.y = y
        self.x = x
        self.side = side
        self.RANGE = RANGE
    
    def check_for_death(self):
        if self.HP <= 0:
            print("Dead")
            return False
        else:
            return True
        
    def check_range(self, attacker: "Enemy"):
        y_dif = attacker.y - self.y
        x_dif = attacker.x - self.x
        r = 1/((x_dif**2 + y_dif**2)**(-1))
        return r

    def take_dmg(self, attacker: "Enemy"):
        print(f"{attacker.name} is attacking {self.name}")
        if self.check_range(attacker) < attacker.RANGE:
            if (self.DEF - attacker.ATK) < 0:
                self.HP += self.DEF - attacker.ATK
            print(f"{self.name} takes {attacker.ATK} dmg\n")
        else:
            print("Oh no it missed")
    
    def movement_x_check(self): #movment shii
        if self.side == "left":
            x_max = len(board[0]) -1
            x_min = 0
            return [x_max, x_min]
        
        elif self.side == "right":
            x_max = len(board) -1
            x_min = int((len(board[0])/2))
            return [x_max, x_min]
        
    # def move_check(self, dif: int, position: int): #movment shii
    #     if y_dif > 0:
    #         if dif < self.SPEED:
    #             self.y += abs(dif)
    #         else:
    #             self.y += self.SPEED
    #     elif y_dif < 0:
    #         if abs(dif) < self.SPEED:
    #             self.y -= abs(dif)
    #         else:
    #             self.y -= self.SPEED

    def move(self, attacker: "Enemy"): #movement shii
        y_dif = attacker.y - self.y
        x_dif = attacker.x - self.x
        movement = self.SPEED
        if y_dif > 0:
            if y_dif < self.SPEED:
                self.y += abs(y_dif)
            else:
                self.y += self.SPEED
            movement -= self.y
        elif y_dif < 0:
            if abs(y_dif) <= self.SPEED:
                self.y -= abs(y_dif)
            else:
                self.y -= self.SPEED
            movement -= self.y
        if movement > 0 and abs(x_dif) > 0:
            if self.side == "left" and self.x < self.movement_x_check()[0]:
                self.x = movement
                if self.x > self.movement_x_check()[0]:
                    self.x = self.movement_x_check()[0]
            if self.side == "right" and self.x > self.movement_x_check()[1]:
                self.x = movement
                if self.x < self.movement_x_check()[1]:
                    self.x = self.movement_x_check()[1]

    def check_stats(self):
        print(f"Name: {self.name}")
        print(f"HP: {self.HP}\n")
    
    def print_encounter(self, attacker: "Enemy"):
        self.check_stats()
        attacker.check_stats()


def nr_check(current_enemy: int, enemy_numbers: int):
    enemy_numbers -= 1
    if (current_enemy + 1) <= enemy_numbers:
        return 1
    elif (current_enemy + 1) > enemy_numbers:
        return 0

def fight(enemy_one, enemy_two):
    index = random.randint(0, 1)
    enemy_list = [enemy_one, enemy_two]
    defender: "Enemy" = enemy_list[index]
    attacker: "Enemy" = enemy_list[nr_check(index, 2)]
    if x == 1:
        defender.print_encounter(attacker)
    defender.take_dmg(attacker)
    defender.check_stats()
    defender.move(attacker)

def place_enemies(enemy_list):
    for enemy in enemy_list:
        y = 0
        x = 0
        enemy: "Enemy"
        for row in board:
            if y == enemy.y:
                for i in row:
                    if x == enemy.x:
                        board[y][x] = "E"
                    x += 1
            y += 1
    return board

def print_map():
    x = 0
    for row in board:
        print(" ")
        for i in row:
            print(i, end=" ")
    print("")

def clear_map():
    board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
    ]
    return board

game = [True, True]

slime = Enemy("Slime", 10, 4, 1, {"Prazil": "Pras"}, 1, random.randint(0, (len(board) -1)), random.randint(0, int((len(board[0])/2 -1))), "left", 1)
goblin = Enemy("Goblin", 15, 5, 0, {"Killswitch": "bam"}, 2,  random.randint(0, (len(board) -1)), random.randint( int((len(board[0])/2)), int((len(board[0])-1))), "right", 2)

x = 0

while game == [True, True]:
    place_enemies([slime, goblin])
    print_map()
    x += 1
    distance = print(slime.check_range(goblin))
    fight(slime, goblin)
    game = [slime.check_for_death(), goblin.check_for_death()]
    board = clear_map()

    #Yay, it kinda works