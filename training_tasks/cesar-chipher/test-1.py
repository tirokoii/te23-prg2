alphabet = "abcdefghijklmnopqurstuvwxyz"
key = 1
check = ""

def error_check(string):
    while True:
        for i in string:
            try:
                crypt_index = alphabet.index(i) + 1
            except ValueError:
                return print("You have used an invalid symbol")
        try:
            message = str(string)
            return message
        except ValueError:
            return print("You have used a number")
        
def index_out_of_range(index_place):
    if index_place == (len(alphabet) - 1):
        return (-2 + key)
    elif index_place == 0:
        if key == 1:
            return len(alphabet)
        else:
            return len(alphabet) - key
            
    else:
        return index_place

def crypt_message(message):
    crypted_message = ""
    for i in message:
        # get out letter
        current_index = alphabet.index(i)
        current_index = index_out_of_range(current_index)
        crypted_message += alphabet[current_index + key]
    return crypted_message

def uncrypt_message(crypt):
    original_message = ""
    for i in crypt:
        current_index = alphabet.index(i)
        current_index = index_out_of_range(current_index)
        original_message += alphabet[current_index - key]
    return original_message

crypted_message = crypt_message("xxx")
original_message = uncrypt_message(crypted_message)
print("crypted message: " + crypted_message + ", " + "message: " + original_message)