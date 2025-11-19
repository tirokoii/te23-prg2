# Anna har N bilar utan däck
# Simon har M reserv däck
def ärint(msg):
    while True :
        try :
            valtVärde = int(input(f"{msg}: "))
            return valtVärde
        except ValueError :
            print("Felaktigt tal")

bilar = ärint("Antal bilar som Anna har: ")
reserv_deck = ärint("Antal däck som Simon har: ")

x = 0

for bil in range(bilar):
    reserv_deck -= 4
    x += 1
    if reserv_deck <= 0:
        break

print(f"{x} bilar blir fullstandiga")

# f(x) = x - a+b

bilantal = 2934
däck = 12
hjul = 4

if däck/hjul < bilantal:
    print(f"{round(däck/hjul)} bilar blir ful")
else:
    print(f"{bilantal} bilar blir ful")

