# Who likes cats and dogs
# Reveal amount

amount_people = int(input("How many people are there: "))
people_dict = {}
people_list = []
cat_counter = 0
dog_counter = 0

for i in range(amount_people):
    name = input("What is your name: ")
    animal = input("Cat or dog: ")
    people_dict[name] = animal
    people_list.append(people_dict[name])

for i in range(people_dict):
    if people_dict[name] == "Cat":
        cat_counter += 1
    elif people_dict[name] == "Dog":
        dog_counter += 1

print(f"There are {cat_counter} cat lovers")
print(f"There are {dog_counter} dog lovers")

