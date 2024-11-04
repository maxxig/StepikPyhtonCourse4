from string import ascii_lowercase, ascii_uppercase
import operator
class CaesarCipher:
    def __init__(self, num):
        self.num = num
    def encode(self, text):
        return self.calc(text, operator.add)

    def decode(self, text):
        return self.calc(text, operator.sub)

    def calc(self, text, f:operator):
        _res = ''
        for t in text:
            if t in ascii_lowercase:
                new_t = ascii_lowercase[f(ascii_lowercase.index(t),self.num) % 26]
                _res += new_t
            elif t in ascii_uppercase:
                new_t = ascii_uppercase[f(ascii_uppercase.index(t),self.num) % 26]
                _res += new_t
            else:
                _res += t
        return _res