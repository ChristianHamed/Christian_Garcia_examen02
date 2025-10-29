class Palindrome:

    def __init__(self, phrase):
        self.phrase = phrase

    def is_palindrome(self) -> bool:
        p = self.phrase
        #Si es palíndromo retorno true
        #y si no retorna false
        if p == "palíndromo":
            return True
        else:
            return False