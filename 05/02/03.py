class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    def __str__(self):
        return f'Вектор на плоскости с координатами ({self.x}, {self.y})'

# TEST_3:
vectors = [Vector(1, 2), Vector(3, 4), Vector(-1, 1), Vector(0, 0), Vector(-100, -100), Vector(25.5, -10.2), Vector(100.0, 0.5)]

for vector in vectors:
    print(vector)

# TEST_4:
vectors = [Vector(1, 2), Vector(3, 4), Vector(-1, 1), Vector(0, 0), Vector(-100, -100), Vector(25.5, -10.2), Vector(100.0, 0.5)]

print(vectors)

# TEST_5:
array = [(76, 164), (61, 124), (91, 192), (19, 158), (114, 142), (106, 49), (91, 43), (84, 35), (170, 24), (130, 116),
         (101, 191), (167, 148), (137, 107), (190, 21), (145, 170), (25, 15), (12, 20), (181, 97), (133, 155),
         (132, 195)]

for x, y in array:
    vector = Vector(x, y)
    print(repr(vector), vector, sep='; ')