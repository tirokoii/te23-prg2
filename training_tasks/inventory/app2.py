class Inventory:
    def __init__(self, content: list):
        self.content = content
        self.size = 10
    
    # def add_item(self, item: "Item"):
    #     if len(self.content) < self.size:
    #         self.content.append(item)
    #     else:
    #         print("Warning! Your inventory is full\n")

    def add_items(self, items: list):
        if len(self.content) < self.size:
            for i in items:
                self.content.append(i)
        else:
            print("Warning! Your inventory is full\n")

    def remove_item(self, item: "Item"):
        if len(self.content) > 0:
            for i in self.content:
                if i == item:
                    self.content.remove(i)

    def inspect(self):
        if len(self.content) == 0:
            print("You have no items in your inventory\n")
        else:
            print("Your Inventory: \n")
            for item in self.content:
                item: "Item"
                print(f"name: {item.name}\ntype: {item.type}\ndescription: {item.description}\n")

    def get_contents(self):
        return self.content
        
class Item:
    def __init__(self, name, type, description, cost):
        self.name = name
        self.type = type
        self.description = description
        self.cost = cost
    
    def inspect(self):
        print(f"Thing: {self.name}\nType: {self.type}\nDescription: {self.description}")
    
    def use(self):
        print(f"You are now using your {self.name}\n")
        inventory.remove_item(self)
        
Gronky = Item("Gronky", "Word", "It's a good word", 0)
Flamp = Item("Flamp", "weapon", "It has a sharp tongue", 20)

inventory = Inventory([])

# inventory.add_item(Gronky)
# inventory.add_item(Flamp)

inventory.add_items([Gronky, Flamp])
