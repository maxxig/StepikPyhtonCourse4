import math
class QuadraticPolynomial:
    def __init__(self, a = 0, b = 0, c = 0):
        self.a, self.b, self.c = float(a), float(b), float(c)

    @classmethod
    def from_iterable(cls, obj):
        # return QuadraticPolynomial(obj[0], obj[1], obj[2])
        return QuadraticPolynomial(*obj)
    @classmethod
    def from_str(cls, s):
        # a, b, c = s.split()
        return QuadraticPolynomial(*s.split())

# TEST_5:
polynom = QuadraticPolynomial.from_iterable([25, 132, -18])

print(polynom.a)
print(polynom.b)
print(polynom.c)