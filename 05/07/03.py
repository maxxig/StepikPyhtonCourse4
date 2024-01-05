from functools import total_ordering
@total_ordering
class RomanNumeral:
    @staticmethod
    def to_roman(number):
        roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                           'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                           'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        roman = ''
        for letter, value in roman_numbers.items():
            while number >= value:
                roman += letter
                number -= value
        return roman
    @classmethod
    def roman_to_arabic(cls, roman):
        integers = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        result = 0
        for i, c in enumerate(roman):
            if i + 1 < len(roman) and integers[roman[i]] < integers[roman[i + 1]]:
                result -= integers[roman[i]]
            else:
                result += integers[roman[i]]
        return int(result)
    def __init__(self, number):
        self.number = number
    def __str__(self):
        return str(self.number)
    def __int__(self):
        return self.roman_to_arabic(self.number)
    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self.roman_to_arabic(self.number) == self.roman_to_arabic(other.number)
        else:
            return NotImplemented
    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return self.roman_to_arabic(self.number) < self.roman_to_arabic(other.number)
        else:
            return NotImplemented
    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            summa = self.roman_to_arabic(self.number) + self.roman_to_arabic(other.number)
            return RomanNumeral(RomanNumeral.to_roman(summa))
        else:
            return NotImplemented
    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            subb = self.roman_to_arabic(self.number) - self.roman_to_arabic(other.number)
            return RomanNumeral(RomanNumeral.to_roman(subb))
        else:
            return NotImplemented

# TEST_10:
roman = RomanNumeral('L')
print(roman.__eq__(1))
print(roman.__ne__(1.1))
print(roman.__gt__(range(5)))
print(roman.__lt__([1, 2, 3]))
print(roman.__ge__({4, 5, 6}))
print(roman.__le__({1: 'one'}))