# Who likes cats and dogs
# Reveal amount

amount_people = int(input("How many people are there: "))
people_dict = {}
people_list = []
cat_counter = 0
dog_counter = 0
cat_lover_list = []
dog_lover_list = []

for i in range(amount_people):
    name = input("What is your name: ")
    animal = input("Cat or dog: ").capitalize()
    people_dict[name] = animal
    people_list.append(people_dict[name])

for key, value in people_dict.items(): #
    if value == "Cat":
        cat_counter += 1
        cat_lover_list.append(key)
    elif value == "Dog":
        dog_counter += 1
        dog_lover_list.append(key)


# for animal_type in people_dict.values(): # 
#     if animal_type == "Cat":
#         cat_counter += 1
#     elif animal_type == "Dog":
#         dog_counter += 1
     
print(f"There are {cat_counter} cat lovers")
for i in cat_lover_list:
    print(i, end=" ")
print(f"\nThere are {dog_counter} dog lovers")
for i in dog_lover_list:
    print(i, end="")

