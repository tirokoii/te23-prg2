alphabet = "abcdefghijklmnopqrstuvwxyz"
key = 10
check = ""

def error_check(letter):
    while True:
        try:
            crypt_index = alphabet.index(letter)
        except ValueError:
            return False
        try:
            message = str(letter)
            return message
        except ValueError:
            return print("You have used a number")
        
def index_out_of_range(i, key):
    alp = (i + key) % len(alphabet)
    return alp

def crypt_message(message):
    crypted_message = ""
    for letter in message:
        # get out letter
        if error_check(letter) != False:
            current_index = alphabet.index(letter)
            current_index = index_out_of_range(current_index, key)
            crypted_message += alphabet[current_index]
        else:
            crypted_message += letter
    return crypted_message

def uncrypt_message(crypt):
    original_message = ""
    for letter in crypt:
        if error_check(letter) != False:
            current_index = alphabet.index(letter)
            current_index = index_out_of_range(current_index, -key)
            original_message += alphabet[current_index]
        else:
            original_message += letter
    return original_message

crypted_message = crypt_message("flexing is wrong")
original_message = uncrypt_message(crypted_message)
print("crypted message: " + crypted_message + ", " + "message: " + original_message)