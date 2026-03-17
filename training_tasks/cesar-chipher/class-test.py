class Cescar:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.decrypt_msg = ""
        self.encrypt_msg = ""
    
    def _error_check(self, letter):
        while True:
            try:
                crypt_index = self.alphabet.index(letter)
            except ValueError:
                return False
            try:
                message = str(letter)
                return message
            except ValueError:
                return print("You have used a number")
    
    # Shift needs (msg, key)
    def _shift(self, msg: str, key: int) -> str:
        result = ""
        for letter in msg.lower():
            if self._error_check(letter) != False:
                new_position = (self.alphabet.index(letter) + key) % len(self.alphabet)
                result += self.alphabet[new_position]
            else:
                result += letter
        return result
                

    def encrypt(self, msg: str, key: int) -> str:
        self.encrypt_msg = self._shift(msg, key)
        return self._shift(msg, key)
    
    def decrypt(self, msg: str, key: int) -> str:
        self.decrypt_msg = self._shift(msg, -key)
        return self._shift(msg, -key)
    
    def brute_force(self, msg: str, max: int):
        for i in range(1, max + 1):
            print(f"{i}: {cescar.encrypt(msg, i)}")
    
cescar = Cescar()

cescar.brute_force("e zkj'p ywna e dwra ikjau", 20)