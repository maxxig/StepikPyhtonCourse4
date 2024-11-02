from math import sqrt
class Vector:
    def __init__(self, *args):
        self.coord = args
    def __str__(self):
        return '(' + ', '.join([str(c) for c in self.coord]) + ')'
    def norm(self):
        return sqrt(sum([s**2 for s in self.coord]))

    def __add__(self, other):
        if len(self.coord) != len(other.coord):
            raise ValueError('Векторы должны иметь равную длину')
        else:
            new_arg = [i+j for i,j in zip(self.coord, other.coord)]
            return Vector(*new_arg)
    def __sub__(self, other):
        if len(self.coord) != len(other.coord):
            raise ValueError('Векторы должны иметь равную длину')
        else:
            new_arg = [i-j for i,j in zip(self.coord, other.coord)]
            return Vector(*new_arg)
    def __mul__(self, other):
        if len(self.coord) != len(other.coord):
            raise ValueError('Векторы должны иметь равную длину')
        else:
            res = sum([i*j for i,j in zip(self.coord, other.coord)])
            return res
    def __eq__(self, other):
        if len(self.coord) != len(other.coord):
            raise ValueError('Векторы должны иметь равную длину')
        else:
            res = all(i==j for i,j in zip(self.coord, other.coord))
            return res