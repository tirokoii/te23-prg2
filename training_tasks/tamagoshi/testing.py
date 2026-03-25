import random
class Test():
    def __init__(self, name):
        self.name = name
        self.conditions = {"happy": False, "angry": True}


te = Test("gogo")
te.conditions["happy"] = True
print(te.conditions["happy"])

print((round(60/10)))
list = [True, False]
print(random.choice([True, False]))