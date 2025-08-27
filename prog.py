def int_check(use): #Man hade nog kunnat optimera denna
    if use == "li":
        try:
            user_inp = int(input("Choose a number between 1-3: "))
            if user_inp == 1 or user_inp == 2 or user_inp == 3:
                number_list.append(user_inp)
                print("Number successfully added")
            else:
                print("Its not possible to use that number")
            return number_list
        except ValueError:
            print("Not a number")
    else:
        try:
            user_inp = int(input("How many numbers would you like to add?: "))
            return user_inp
        except ValueError:
            print("Not a number")
            

def print_list(the_list):
    for i in the_list:
        print(i)
    print(f"You have {len(the_list)} of the number {i}")

number_list = []

one_list = []
two_list = []
three_list = []
smallest_number = 1
number_times = int_check("num") #Fler val vad kul!
game = "y"

while game == "y":
    while len(number_list) < number_times: #Optimerade den, kan sätta in bara 10 som konstant
        user_inp = int_check("li") #Jag vet att det är lite vagt med "li" och "num", men man tar det man har

    number_list.sort()

    for i in number_list:
        if i == smallest_number:
            one_list.append(i)
        elif i == smallest_number + 1:
            two_list.append(i)
        else:
            three_list.append(i)

    print("Your numbers: ") 
    print_list(one_list) #Hade man kunnat optimera detta? Troligtvis
    print_list(two_list)
    print_list(three_list)

    game = input("Do you want to continue? [y/n]: ")
    
 

    

