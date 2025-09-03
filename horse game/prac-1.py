# Ask user for name
# Name must be at least 2 letters long
# Otherwise user has to re write name

name_ok = False

def name_check(prompt):
    while True:
        name = input(prompt)
        if len(name) >= 2:
            return name

while name_ok is False:
    input_name = input("What is your name: ")
    if len(input_name) >= 2:
        name_ok = True