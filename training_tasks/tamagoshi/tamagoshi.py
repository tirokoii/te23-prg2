import random

diseases = []

class Tamagoshi():
    def __init__(self, 
                 name: str, 
                 age: int,
                 max_age: int, 
                 max_health: int, 
                 health: int, 
                 happiness: int, 
                 max_happiness: int, 
                 hunger: int, 
                 max_hunger: int, 
                 is_alive: bool = True,
                 conditions = {"is_bored": True,
                                "is_scared": False,
                                "is_playful": False, 
                                "is_angry": False, 
                                "is_messy": False, 
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
        self.hunger = max(0, self.hunger - max(20, random.randint(1, 6) * 4))
        self.happiness = min(self.max_happiness, self.health + min(10, random.randint(1, 6) * 4))

    
    def feed(self):
        self.health = min(self.max_health, self.health + max(10, random.randint(1, 10) * 2))
        self.happiness = min(self.max_happiness, self.happiness + max(10, random.randint(1, 4) * 4))
        self.hunger = max(0, self.hunger + max(15, random.randint(1, 6) * 4))
        self.conditions["is_bored"] = True
        self.conditions["is_mess"] = True
        self.conditions["is_playful"] = False
        self.conditions["is_angry"] = False
    
    def play(self):
        self.conditions["is_bored"] = False
        self.conditions["is_playful"] = False
        self.conditions["is_angry"] = False
        self.happiness = min(self.max_happiness, self.happiness + max(11, random.randint(1, 5) * 4))
        self.hunger = max(0, self.hunger - max(10, random.randint(1 ,10) * 2))

        chance_of_mess = random.randint(1, 10)

        if chance_of_mess > 4 < 5:
            self.conditions["is_mess"] = True
    
    def pet(self):
        self.conditions["is_bored"] = False
        self.conditions["is_playful"] = True
        self.conditions["is_scared"] = False
        self.happiness = min(self.max_happiness, self.happiness + max(11, random.randint(1, 5) * 4))
        self.hunger = min(self.max_hunger, self.hunger + max(5, random.randint(1, 4) * 3))
    
    def clean(self):
        self.conditions["is_mess"] = False
        self.conditions["is_bored"] = True
        self.conditions["is_scared"] = True
        self.conditions["is_playful"] = True
        self.happiness = max(0, self.happiness - max(11, random.randint(1, 5) * 4))
    
    def go_to_vet(self):
        self.happiness = max(0, self.health - max(20, random.randint(1, 6) * 4))
        self.hunger = max(0, self.hunger - max(10, random.randint(1, 4) * 4))
        self.conditions["is_scared"] = True
        self.conditions["is_mess"] = True
    
    def health_check(self):
        if self.hunger < self.max_hunger / 2:
            self.health = max(0, self.health - max(10, random.randint(3, 8) * 5))
        if self.happiness < self.max_happiness / 1.2:
            self.health = max(0, self.health - max(5, random.randint(1, 4) * 2))

        # Add in rounds for if_mess so that the amount of rounds that it is a mess it gets sick

    def check_if_alive(self):
        if self.health == 0:
            self.is_alive = False

    def check_conditions(self):
        condition_sentence = ""
        for condition in self.conditions:
            condition_sentence = ""
            if self.conditions[condition] == True:
                for letter in condition:
                    if letter == "_":
                        condition_sentence += " "
                    else:
                        condition_sentence += letter

                print(self.name + " " + condition_sentence + ", you need to do something")
        print(f"{self.name} has {self.happiness}/{self.max_happiness} happiness, {self.hunger}/{self.max_hunger} hunger and {self.health}/{self.max_health} health")
        self.health_check()
        # Add in rounds to have condition actually do something depending on how many rounds the pet has had it

class Game():
    def __init__(self, pet: Tamagoshi = None, day: int = 0, round: int = 0, max_rounds: int = 3, game_state: str = "starting"):
        self.pet = pet
        self.day = day
        self.round = round
        self.max_rounds = max_rounds
        self.game_state = game_state

    def game_check(self):
        if self.pet.is_alive == False:
            self.game_state = "wait"
        if self.game_state == "wait":
            print(f"You killed {self.pet.name}")
            print("Do you want to continue? [y/n]")
            choice = input(" ")
            if choice == "y":
                self.game_state = "restart"
            elif choice == "n":
                self.game_state = "quit"

        if self.game_state == "restart":
            pass # get pet

        if self.game_state == "quit":
            print("Goodbye")

    def start_game(self):
        #Choosing Tamagoshi traits
        continuing = False
        while continuing == False:
            print("What is your pets name?")
            name = input("")
            print(f"Are you sure that you want to name your pet {name}? [y/n]")
            choice = input("")
            if choice == "y":
                print(f"You are ready to welcome {name} into your life")
                continuing = True
            elif choice == "n":
                continuing = False


        age = random.randint(0, 5)
        max_age = min(21, (random.randint(4, 12) * 2))
        max_health = min(68, (random.randint(1, 10) * 12))
        health = min((random.randint(1, 7) * 10), max_health)
        max_happiness = 100
        happiness = min((random.randint(1, 20) * 5), max_happiness)
        max_hunger = max(73, random.randint(10, 20) * 6)
        hunger = min(random.randint(1, 20) * 5, max_hunger)

        # Adding Tamagoshi traits
        self.pet = Tamagoshi(name, age, max_age, max_health, health, happiness, max_happiness, hunger, max_hunger, conditions= { 
            "is_bored": random.choice([True, False]),
            "is_scared": random.choice([True, False]),
            "is_playful": random.choice([True, False]),
            "is_angry": random.choice([True, False]),
            "is_messy": False,
            "is_digesting": False,
            "is_sick": False
            })
        
        print("")
        
    def game_loop(self):
        while self.round <= self.max_rounds and self.game_state == "running":
            self.pet.check_if_alive()
            self.game_check()
            self.pet.check_conditions()
            print("What do you want to do with your pet? [pet/play/feed/go to vet/clean]")

            continuing = False
            while continuing == False:
                choice = input("")
                if choice == "pet":
                    self.pet.pet()
                    continuing = True
                elif choice == "play":
                    self.pet.play()
                    continuing = True
                elif choice == "feed":
                    self.pet.feed()
                    continuing = True
                elif choice == "go to vet":
                    self.pet.go_to_vet()
                    continuing = True
                elif choice == "clean":
                    self.pet.clean()
                    continuing = True
                else:
                    print("not a choice")
                    continuing = False
            self.round += 1

        print(f"{self.pet.name} has grown one year older! Its now {self.pet.age}")
        self.pet.age += 1
        self.round = 0
    

game = Game()

while game.game_state != "quit":
    if game.game_state == "starting":
        game.start_game()
        game.game_state = "running"
    game.game_loop()

