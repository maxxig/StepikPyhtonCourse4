from functools import total_ordering
@total_ordering
class Word:
    def __init__(self, word):
        self.word = word
    def __repr__(self):
        return f"Word('{self.word}')"
    def __str__(self):
        return self.word.capitalize()

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        else:
            return NotImplemented

word = Word('Beegeek')

print(word.__eq__(1))
print(word.__ne__(1.1))
print(word.__gt__(range(5)))
print(word.__lt__([1, 2, 3]))
print(word.__ge__({4, 5, 6}))
print(word.__le__({1: 'one'}))