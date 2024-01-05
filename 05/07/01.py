class Vector:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __bool__(self):
        return True if self.x != 0 or self.y !=0 else False
    def __int__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)
    def __float__(self):
        return float((self.x ** 2 + self.y ** 2) ** 0.5)
    def __complex__(self):
        return complex(self.x, self.y)

# TEST_5:
vector = Vector(3, -4)

print(vector)
print(int(vector))
print(float(vector))
print(complex(vector))