import random

diseases = []

class Tamagoshi():
    def __init__(self, 
                 name: str, 
                 max_age: int, 
                 max_health: int, 
                 health: int, 
                 happiness: int, 
                 max_happiness: int, 
                 hunger: int, 
                 max_hunger: int, 
                 is_alive = True,
                 age: int = 0,
                 conditions = {"is_bored": True,
                                "is_scared": False,
                                "is_playful": False, 
                                "is_angry": False, 
                                "is_mess": False, 
                                "is_digesting": False,
                                "is_sick": False
                                }):
        
        self.name = name
        self.age = age
        self.max_age = max_age
        self.max_health = max_health
        self.health = health
        self.happiness = happiness
        self.max_happiness = max_happiness
        self.hunger = hunger
        self.max_hunger = max_hunger
        self.is_alive = is_alive
        self.conditions = conditions
    
    def age_increase(self):
        self.age += 1
        self.hunger = max(0, self.hunger - max(20, random.randint(6) * 4))
        self.happiness = min(self.max_happiness, self.health + min(10, random.randint(6) * 4))

    
    def feed(self):
        self.health = min(self.max_health, self.health + max(10, random.randint(10) * 2))
        self.happiness = min(self.max_happiness, self.health + max(10, random.randint(4) * 4))
        self.hunger = max(0, self.hunger - max(15, random.randint(6) * 4))
        self.conditions["is_bored"] = True
        self.conditions["is_mess"] = True
        self.conditions["is_playful"] = False
    
    def play(self):
        self.conditions["is_bored"] = False
        self.conditions["is_playful"] = False
        self.happiness = min(self.max_happiness, self.health + max(11, random.randint(5) * 4))
        self.hunger = min(self.max_hunger, self.hunger + max(10, random.randint(10) * 2))

        chance_of_mess = random(1, 10)

        if chance_of_mess > 4 < 5:
            self.conditions["is_mess"] = True
    
    def pet(self):
        self.conditions["is_bored"] = False
        self.conditions["is_playful"] = True
        self.happiness = min(self.max_happiness, self.health + max(11, random.randint(5) * 4))
        self.hunger = min(self.max_hunger, self.hunger + max(5, random.randint(4) * 3))
    
    def clean(self):
        self.conditions["is_bored"] = True
        self.conditions["is_scared"] = True
        self.conditions["is_playful"] = True
        self.happiness = min(self.max_happiness, self.health + max(11, random.randint(5) * 4))
    
    def go_to_vet(self):
        self.happiness = max(0, self.health - max(20, random.randint(6) * 4))
        self.hunger = max(0, self.hunger - max(10, random.randint(4) * 4))
        self.conditions["is_scared"] = True
        self.conditions["is_mess"] = True
    
    def health_check(self):
        if self.hunger < self.max_hunger/2:
            self.health = max(0, self.health - max(10, random.randint(3, 8) * round(self.max_hunger / self.hunger)))
        elif self.happiness < self.max_happiness / 1.2:
            self.health = max(0, self.health - max(5, random.randint(4) * round(self.max_happiness / self.happiness)))
        # Add in rounds for if_mess so that the amount of rounds that it is a mess it gets sick

    def check_if_alive(self):
        if self.health == 0:
            self.is_alive = False

    def check_conditions(self):
        condition_sentence = ""
        for condition in self.conditions:
            if self.conditions[condition] == True:
                for letter in condition:
                    if letter == "_":
                        condition_sentence += " "
                    else:
                        condition_sentence += letter

                print(self.name + " " + condition_sentence + ", you need to do something")
        # Add in rounds to have condition actually do something depending on how many rounds the pet has had it

your_pet = Tamagoshi("Pippy", 12, 60, 60, 100, 100, 0, 40)

class Game():
    def __init__(self, pet: Tamagoshi, day: int = 0, round: int = 0, max_rounds: int = 3, game = True):
        self.pet = pet
        self.day = day
        self.round = round
        self.max_rounds = max_rounds
        self.game = True

    def game_check(self):
        if self.pet.is_alive == False:
            self.game = True


    def game_loop(self):
        while self.max_rounds != 0:
            self.game_check()
            self.pet.check_if_alive
            self.pet.check_conditions
            round += 1
    

