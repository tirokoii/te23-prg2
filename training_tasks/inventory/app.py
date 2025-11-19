class Object_lust: #Object_list
    def __init__(self, content: list, size: int):
        self.content = content
        self.size = 20

    def add_item(self, item): 
        if len(self.content) <= self.size:
            self.content.append(item)
        else:
            print("WARNING!\nYour inventory is to full, you need to discard an item")
        
    def remove_item(self, item: "Item"):
        self.content.remove(item)
    
class Item:
    def __init__(self, name: str, type: str, perks: list, description: str, cost: int):
        self.name = name
        self.type = type
        self.perks = perks
        self.description = description
        self.cost = 0
        self.equipped = False

    def use(self, game_object: "Game_object", relic: "Relics"):
        if type == "weapon":
            if game_object.weapon.equipped == False:
                for perk in self.perks:
                    perk: dict
                    if perk == "health":
                        game_object.hp += perk["health"]
                    elif perk == "strength":
                        game_object.ATK += perk["strength"]
                    elif perk == "speedy":
                        game_object.SPEED += perk["speedy"]
                    else:
                        print("No perk")
            else:
                answer = input(f"Do you want to switch out your current weapon {game_object.weapon.name} for the {self.name}?n [y/n] ")
                if answer == "y":
                    game_object.weapon.equipped == False
                    self.equipped == True
                    game_object.inventory.append(game_object.weapon)
                    game_object.weapon = self
                elif answer == "n":
                    print("Okay")

        elif type == "relic":
            relic.add_item()

        elif type == "collectible":
            print("You can't use this item")
        else:
            pass


class Game_object:
    def __init__(self, name:str, HP:int, ATK:int, ATK_SPEED: int, SPEED: int, parry: bool, inventory: list, weapon: Item, relics: "Relics", money: int, upgrades: list):
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.ATK_SPEED = ATK_SPEED
        self.SPEED = SPEED
        self.parry = parry
        self.inventory = inventory
        self.weapon = weapon
        self.relics = relics
        self.money = money
        self.upgrades = upgrades


class Upgrade:
    def __init__(self, content: list, size: int):
        self.content = content
        self.size = 10

    def add_item(self): 
        if len(self.content) <= self.size:
            self.content.append(self.upgrade)
        else:
            print("WARNING!\nYou have too many upgrades")
        
    def remove_item(self):
        self.content.remove(self.upgrade)

class Relics:
    def __init__(self, content: list, size: int):
        self.content = content
        self.size = 3

    def add_item(self, relic): 
        if len(self.content) <= self.size:
            self.content.append(relic)
        else:
            print("WARNING!\nYou have too many upgrades")
        
    def remove_item(self, relic):
        self.content.remove(relic)

# Dammit, jbfebiarhbqerfhiorbgiuqerghargmqcnvhtbwyuqibgyuiöpwbvfvuibvfyuawkbftyceaycarvgbialrefbvhvjbagihebaöibaoirvlgagpäarg