class Vector:
    def __init__(self, x, y):
        if isinstance(x, int|float) and isinstance(y, int|float):
            self.x, self.y = x, y
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple) and len(other) == 2:
            return self.x == other[0] and self.y == other[1]
        else:
            return NotImplemented

# TEST_7:
a = Vector(1, 2)
b = Vector(3, 4)
c = Vector(5, 6)

vectors = [a, b, c]
print(vectors)

# TEST_8:
vector = Vector(0, 1)

print(vector.__eq__(1))
print(vector.__ne__(1.1))
print(vector.__gt__(range(5)))
print(vector.__lt__([1, 2, 3]))
print(vector.__ge__({4, 5, 6}))
print(vector.__le__({1: 'one'}))
