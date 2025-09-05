
# word = input("Write a word: ")

letters = []
# x = len(word) - 1

# for i in range(len(word)):
#     letters.append(word[x])
#     x -= 1

# print(letters)

word = input("Write a word: ")

for i in range(len(word)): 
    letters.append(word[-(i+1)]) #Apparently index 0 = index -5. OK

print(letters)