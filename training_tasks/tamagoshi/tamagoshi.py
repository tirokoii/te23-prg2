import random

diseases = []

class Tamagoshi():
    def __init__(self, name, max_age, health, max_health, happiness, max_happiness, hunger, max_hunger):
        self.name = name
        self.age = 0
        self.max_age = max_age
        self.max_health = max_health
        self.health = health
        self.happiness = happiness
        self.max_happiness = max_happiness
        self.hunger = hunger
        self.max_hunger = max_hunger
        self.conditions = {"is_bored": True, "is_scared": False, "is_playful": False, "is_angry": False, "is_mess": False, "is_digesting": False}
    
    def age_increase(self):
        self.age += 1
    
    def feed(self):
        self.health = min(self.max_health, self.health + max(10, random.randint(10) * 2))
        self.happiness = min(self.happiness, self.health + max(5, random.randint(4) * 2))
        self.hunger = max(0, self.hunger - max(15, random.randint(6) * 4))
        self.conditions["is_bored"] = True
        self.conditions["is_mess"] = True
    
    def play(self):
        self.conditions["is_bored"] = False
        self.happiness = min(self.happiness, self.health + max(11, random.randint(5) * 4))
        self.hunger = min(self.max_hunger, self.hunger + max(10, random.randint(10) * 2))

        chance_of_mess = random(1, 10)

        if chance_of_mess > 4 < 5:
            self.conditions["is_mess"] = True
    
    def pet(self):
        self.conditions["is_bored"] = False
        self.happiness = min(self.happiness, self.health + max(11, random.randint(5) * 4))
        self.hunger = min(self.max_hunger, self.hunger + max(5, random.randint(4) * 3))
    
    def clean(self):
        self.conditions["is_bored"] = True
