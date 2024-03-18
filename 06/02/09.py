class MutableString:
    def __init__(self, string=''):
        self._string = string
    def lower(self):
        self._string = self._string.lower()
    def upper(self):
        self._string = self._string.upper()
    def __repr__(self):
        return f"MutableString('{self._string}')"
    def __str__(self):
        return self._string
    def __len__(self):
        return len(self._string)
    def __iter__(self):
        return iter(self._string)
    def __getitem__(self, key):
        if isinstance(key, slice):
            return MutableString(self._string[key])
        return self._string[key]
    def __setitem__(self, key, value):
        if isinstance(key, slice):
            l = [item for item in self._string]
            l[key] = value
            self._string = ''.join(l)
        else:
            if key < 0 :
                while(key < 0):
                    key += len(self._string)
            self._string = self._string[:key] + value + self._string[key + 1:]
        # self._string = ''.join((map(lambda x: x if self._string.index(x) != key else value, self._string)))

    def __delitem__(self, key):
        if isinstance(key, slice):
            l = [item for item in self._string]
            del l[key]
            self._string = ''.join(l)
        else:
            self._string = ''.join(x for x in self._string if self._string.index(x) != key)
    def __add__(self, other):
        if isinstance(other, MutableString):
            return MutableString(self._string + other._string)
        else:
            return NotImplemented

# INPUT DATA:

# TEST_1:
mutablestring = MutableString('beegeek')

print(*mutablestring)
print(str(mutablestring))
print(repr(mutablestring))

# TEST_2:
mutablestring = MutableString('Beegeek')

mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)

# TEST_3:
mutablestring1 = MutableString('bee')
mutablestring2 = MutableString('geek')

print(mutablestring1 + mutablestring2)
print(mutablestring2 + mutablestring1)

# TEST_4:
mutablestring = MutableString('beegeek')

print(mutablestring)
mutablestring[0] = 'B'
mutablestring[-4] = 'G'
print(mutablestring)

# TEST_5:
mutablestring = MutableString('beegeek')

s1 = mutablestring[2:]
s2 = mutablestring[:5]
s3 = mutablestring[2:5:2]

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))

# TEST_6:
mutablestring = MutableString('Ada Wong')
id1 = id(mutablestring)

mutablestring.upper()
id2 = id(mutablestring)

print(id1 == id2)

# TEST_7:
string = '''For a long time it was a mystery to me how something very expensive and technologically advanced could be 
so useless. And I soon realized that a computer is a stupid machine that has the ability to do incredibly smart things, 
while programmers are smart people who have a talent for doing incredibly stupid things. In short, 
they found each other.
Bill Bryson'''

mutablestring1 = MutableString(string)
mutablestring2 = mutablestring1[20:45]

print(mutablestring1 is mutablestring2)

# TEST_8:
string = '''Sometimes it's better to stay home on Monday than to spend the whole week debugging code written on Monday.
Christopher Thompson'''
mutablestring = MutableString(string)

print(mutablestring[30], mutablestring[3], mutablestring[66], mutablestring[66], mutablestring[1], sep='')

# TEST_9:
string = '''Many of you are familiar with the virtues of being a programmer. There are only three of them, 
and of course this is: laziness, impatience and pride. Larry Wall'''
mutablestring = MutableString(string)

print(mutablestring[20])
print(mutablestring[-30])
print(mutablestring[:11])
print(mutablestring[16:])
print(mutablestring[4::10])
print(mutablestring[::-10])

# TEST_10:
string1 = MutableString('Разбежавшись')
string2 = MutableString('прыгну')
string3 = MutableString('со скалы')

array = [string1, string2, string3]
print(array)

# TEST_11:
mutablestring = MutableString()
print(repr(mutablestring))

# TEST_12:
mutablestring = MutableString('beegeek')

del mutablestring[2:5]
del mutablestring[1:5:2]
print(mutablestring)

# TEST_13:
mutablestring = MutableString('beegeek')

mutablestring[-1] = 'ee'
print(mutablestring)

mutablestring[-2:] = 'geek'
print(mutablestring)

# TEST_14:
mutablestring = MutableString('beegeek')

del mutablestring[1:3]
print(mutablestring)