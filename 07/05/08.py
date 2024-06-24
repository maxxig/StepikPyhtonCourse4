from collections.abc import Sequence, Iterable
import copy

class SortedList(Sequence):
    def sort(self):
        self._iterable = sorted(self._iterable, key=lambda x: x)
    def __init__(self, iterable = []):
        self._iterable = copy.deepcopy(iterable)
        self.sort()
    def __getitem__(self, item):
        return self._iterable[item]
    def __delitem__(self, item):
        del self._iterable[item]
        self.sort()
    def __setitem__(self, key, value):
        raise NotImplementedError
    def __len__(self):
        return len(self._iterable)
    def __repr__(self):
        return f'SortedList({self._iterable})'
    def add(self, item):
        if isinstance(item, int):
            self._iterable.append(item)
        elif isinstance(item, Iterable):
            self._iterable.extend(item)
        self.sort()
    def discard(self, _it):
        self._iterable = [item for item in self._iterable if item != _it]
        self.sort()
    def update(self, item):
        self._iterable.extend(item)
        self.sort()
    def append(self, item):
        raise NotImplementedError
    def insert(self, index, item):
        raise NotImplementedError
    def extend(self, item):
        raise NotImplementedError
    def reverse(self):
        raise NotImplementedError
    def __reversed__(self):
        raise NotImplementedError
    def __add__(self, other):
        if isinstance(other, SortedList):
            return SortedList(self._iterable + other._iterable)
        else:
            return NotImplemented
    def __iadd__(self, other):
        if isinstance(other, SortedList):
            self.add(other._iterable)
            return self
            # return SortedList(self._iterable + other._iterable)
        else:
            return NotImplemented
    def __mul__(self, i):
        if isinstance(i, int):
            return SortedList(self._iterable * i)
        else:
            return NotImplemented
    def __imul__(self, i):
        if isinstance(i, int):
            self._iterable = self._iterable * i
            self.sort()
            return self
        else:
            return NotImplemented





# INPUT DATA:

# TEST_1:
numbers = SortedList([5, 3, 4, 2, 1])


print(numbers)
print(numbers[1])
print(numbers[-2])
numbers.add(0)
print(numbers)
numbers.discard(4)
print(numbers)
numbers.update([4, 6])
print(numbers)

# TEST_2:
numbers = SortedList([5, 3, 4, 2, 1])

print(len(numbers))
print(*numbers)
print(1 in numbers)
print(6 in numbers)

# TEST_3:
numbers1 = SortedList([1, 3, 5])
numbers2 = SortedList([2, 4])

print(numbers1 + numbers2)
print(numbers1 * 2)
print(numbers2 * 2)

# TEST_4:
numbers = SortedList([5, 4, 3, 2, 1])

print(numbers)
del numbers[1]

print(numbers)
del numbers[-1]

print(numbers)

try:
    numbers[0] = 7
except NotImplementedError:
    print('Неподдерживаемая операция')

# TEST_5:
numbers = SortedList([1, 2, 3, 4, 5])

try:
    numbers.append(6)
except NotImplementedError:
    print('Неподдерживаемая операция')

# TEST_6:
numbers = SortedList([1, 2, 3, 4, 5])

try:
    numbers.insert(0, 0)
except NotImplementedError:
    print('Неподдерживаемая операция')

# TEST_7:
numbers = SortedList([1, 2, 3, 4, 5])

try:
    numbers.extend([6, 7, 8, 9, 10])
except NotImplementedError:
    print('Неподдерживаемая операция')

# TEST_8:
numbers = SortedList([1, 2, 3, 4, 5])

try:
    numbers.reverse()
except NotImplementedError:
    print('Неподдерживаемая операция')

# TEST_9:
numbers = SortedList([1, 2, 3, 4, 5])

try:
    reversed(numbers)
except NotImplementedError:
    print('Неподдерживаемая операция')

# TEST_10:
numbers = SortedList([5, 4, 3, 2, 1])

numbers.update([5, 4, 3, 2, 1])
print(*numbers)

numbers *= 3
print(*numbers)

numbers.discard(4)
print(*numbers)

# TEST_11:
numbers1 = SortedList([1, 3, 5])
numbers2 = SortedList([2, 4])

id1_numbers1 = id(numbers1)
id1_numbers2 = id(numbers2)

numbers1 += numbers2
numbers2 *= 2

id2_numbers1 = id(numbers1)
id2_numbers2 = id(numbers2)

print(id1_numbers1 == id2_numbers1)
print(id1_numbers2 == id2_numbers2)
print(3 in numbers1)

# TEST_12:
data = [5, 4, 3, 2, 1]
numbers = SortedList(data)

print(numbers)
data.pop()

print(data)
print(numbers)

# TEST_13:
numbers = SortedList()
print(numbers)

# TEST_14:
numbers1 = SortedList([5, 3, 4, 2, 1])
numbers2 = SortedList([10, 9, 8, 7, 6])

numbers1 = numbers1 + numbers2
print(numbers1, type(numbers1))

numbers2 = numbers2 * 2
print(numbers2, type(numbers2))

# TEST_15:
numbers1 = SortedList([5, 3, 4, 2, 1])
numbers2 = SortedList([10, 9, 8, 7, 6])

numbers1 += numbers2
print(numbers1, type(numbers1))

numbers2 *= 2
print(numbers2, type(numbers2))

# TEST_16:
numbers1 = SortedList([5, 3, 4, 2, 1])
numbers2 = SortedList([10, 9, 8, 7, 6])

numbers1 = numbers1 * -100
print(numbers1)

numbers2 *= 0
print(numbers2)

# TEST_17:
numbers = SortedList([5, 3, 4, 2, 1])
print(numbers.__add__(1))
print(numbers.__iadd__(1.1))
print(numbers.__mul__([1, 2, 3]))
print(numbers.__imul__({4, 5, 6}))