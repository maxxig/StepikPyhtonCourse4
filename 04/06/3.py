import math
class QuadraticPolynomial:
    def __init__(self, a = 0, b = 0, c = 0):
        self.a, self.b, self.c = a, b, c

    @property
    def x1(self):
        t = self.b * self.b - 4 * self.a * self.c
        if t < 0:
            return None
        else:
            return (-self.b-math.sqrt(t))/(2 * self.a)

    @property
    def x2(self):
        t = self.b * self.b - 4 * self.a * self.c
        if t < 0:
            return None
        else:
            return (-self.b + math.sqrt(t))/(2 * self.a)

    @property
    def view(self):
        return f'{self.a}x^2 {"+" if self.b >= 0 else "-"} {abs(self.b)}x {"+" if self.c >= 0 else "-"} {abs(self.c)}'

    @property
    def coefficients(self):
        return (self.a, self.b, self.c)
    @coefficients.setter
    def coefficients(self, inp):
        self.a, self.b, self.c = inp


polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (5, 3, 1)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)