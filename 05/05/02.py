class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented
    def __mul__(self, n):
        if isinstance(n, int | float):
            return Vector(self.x * n, self.y * n)
        else:
            return NotImplemented
    def __rmul__(self, other):
        return self.__mul__(other)
    def __truediv__(self, n):
        if isinstance(n, int | float):
            return Vector(self.x / n, self.y / n)
        else:
            return NotImplemented

# TEST_5:
data = [(33, 20, 24), (40, 47, 43), (26, 69, 10), (78, 70, 26), (86, 23, 48), (49, 88, 65), (12, 51, 31),
           (78, 53, 57), (58, 60, 96), (81, 29, 36), (8, 17, 87), (32, 46, 80), (34, 68, 22), (71, 79, 63),
           (21, 78, 31), (83, 42, 74), (47, 69, 90), (49, 40, 94), (46, 90, 33), (81, 98, 18), (44, 66, 9), (5, 52, 65),
           (48, 52, 88), (55, 80, 7), (60, 71, 36), (22, 41, 50), (17, 89, 98), (10, 77, 30), (50, 26, 42),
           (41, 60, 26), (95, 63, 53), (68, 73, 20), (36, 97, 54), (50, 98, 44), (62, 98, 34), (87, 65, 81),
           (73, 76, 44), (37, 67, 28), (22, 5, 70), (65, 83, 80), (91, 91, 26), (79, 94, 60), (56, 69, 47), (18, 6, 50),
           (88, 14, 53), (69, 78, 25), (35, 7, 53), (88, 97, 79), (41, 51, 27), (84, 71, 99), (61, 59, 57),
           (20, 20, 44), (95, 85, 88), (60, 67, 17), (16, 8, 91), (32, 25, 22), (59, 24, 83), (76, 28, 34),
           (28, 42, 87), (52, 19, 89), (18, 61, 98), (89, 9, 51), (66, 8, 95), (90, 79, 32), (76, 74, 63), (35, 51, 68),
           (36, 57, 51), (40, 84, 75), (90, 43, 61), (100, 99, 13), (82, 67, 71), (38, 9, 84), (76, 7, 27),
           (53, 49, 93), (40, 17, 90), (33, 82, 36), (58, 95, 81), (70, 17, 45), (90, 65, 83), (87, 53, 50),
           (90, 8, 32), (88, 21, 44), (18, 72, 24), (16, 91, 13), (80, 20, 53), (63, 13, 81), (6, 90, 15), (96, 82, 87),
           (39, 19, 85), (54, 58, 55), (52, 97, 19), (54, 86, 69), (100, 17, 90), (51, 91, 28), (26, 62, 83),
           (86, 70, 20), (22, 13, 41), (100, 39, 85), (34, 92, 39), (75, 68, 9)]

for x, y, digit in data:
    vector = Vector(x, y)
    print(vector * digit)

# TEST_6:
vectors = [Vector(160, 880), Vector(440, 820), Vector(450, 190), Vector(590, 470), Vector(700, 760), Vector(190, 480),
           Vector(490, 150), Vector(210, 980), Vector(690, 940), Vector(820, 320), Vector(590, 570), Vector(650, 420),
           Vector(520, 200), Vector(380, 870), Vector(1000, 360), Vector(200, 950), Vector(860, 480), Vector(980, 850),
           Vector(420, 950), Vector(500, 460), Vector(140, 520), Vector(280, 1000), Vector(170, 550), Vector(550, 330),
           Vector(60, 470), Vector(890, 60), Vector(880, 140), Vector(170, 170), Vector(210, 950), Vector(720, 960),
           Vector(470, 120), Vector(130, 720), Vector(390, 500), Vector(900, 710), Vector(810, 710), Vector(290, 790),
           Vector(200, 270), Vector(400, 680), Vector(450, 810), Vector(180, 650), Vector(190, 730), Vector(330, 560),
           Vector(560, 260), Vector(830, 120), Vector(600, 220), Vector(460, 300), Vector(950, 130), Vector(300, 340),
           Vector(230, 740), Vector(970, 900), Vector(710, 630), Vector(360, 1000), Vector(740, 580), Vector(370, 450),
           Vector(140, 450), Vector(700, 160), Vector(850, 250), Vector(860, 670), Vector(810, 850), Vector(900, 560),
           Vector(580, 310), Vector(350, 330), Vector(210, 960), Vector(480, 310), Vector(350, 310), Vector(900, 230),
           Vector(300, 270), Vector(1000, 120), Vector(640, 810), Vector(300, 340), Vector(200, 300), Vector(240, 50),
           Vector(250, 890), Vector(110, 320), Vector(950, 450), Vector(250, 200), Vector(170, 970), Vector(350, 90),
           Vector(110, 310), Vector(80, 120), Vector(910, 810), Vector(110, 510), Vector(80, 280), Vector(710, 500),
           Vector(550, 210), Vector(520, 740), Vector(170, 180), Vector(750, 540), Vector(420, 480), Vector(910, 800),
           Vector(420, 490), Vector(870, 780), Vector(630, 570), Vector(460, 820), Vector(340, 730), Vector(440, 100),
           Vector(860, 50), Vector(100, 890), Vector(710, 520), Vector(530, 120)]

for vector in vectors:
    print(vector / 10)

# TEST_7:
vector1 = Vector(5, 10)
vector2 = Vector(10, 15)

vector3 = vector1 - vector2
vector4 = vector2 - vector1

print(vector3)
print(vector4)

# TEST_8:
vector = Vector(10, 20)
print(vector.__add__([]))
print(vector.__sub__(()))
print(vector.__mul__({}))
print(vector.__truediv__(set()))