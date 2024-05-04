class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def perimeter(self):
        return (self.a + self.b + self.c)
class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)
