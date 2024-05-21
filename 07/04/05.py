from collections import UserList
class NumberList(UserList):
    def __init__(self, _iterable=[]):
        if all(map(lambda x: True if isinstance(x, int|float) else False, _iterable)):
            super().__init__(_iterable)
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def __setitem__(self, index, item):
        if isinstance(item, int|float):
            self.data[index] = item
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
    def insert(self, index, item):
        if isinstance(item, int|float):
            self.data.insert(index, item)
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
    def append(self, item):
        if isinstance(item, int|float):
            self.data.append(item)
        elif isinstance(item, list|type(self)) and all(map(lambda x: True if isinstance(x, int | float) else False, item)):
            self.data.append(item)
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def extend(self, other):
        if isinstance(other, type(self)|int|float):
            self.data.extend(other)
        elif isinstance(other, list|type(self)) and all(map(lambda x: True if isinstance(x, int | float) else False, other)):
            self.data.extend(other)
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def add(self, other):
        if isinstance(other, list|type(self)) and all(map(lambda x: True if isinstance(x, int | float) else False, other)):
            return self.data.__add__(other)
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
    def __iadd__(self, other):
        if isinstance(other, list|type(self)) and all(map(lambda x: True if isinstance(x, int | float) else False, other)):
            return self.data.__iadd__(other)
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')



# TEST_9:
numberlist = NumberList([1, 2])
try:
    numberlist.extend([5, '4', 3])
except TypeError as e:
    print(e)

# TEST_10:
n = NumberList([1, 2, 3])

try:
    n[1] = '5'
except TypeError as e:
    print(e)