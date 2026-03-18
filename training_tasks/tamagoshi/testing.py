class Test():
    def __init__(self):
        self.conditions = {"happy": False, "angry": True}


te = Test()
te.conditions["happy"] = True
print(te.conditions["happy"])