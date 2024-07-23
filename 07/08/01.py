class Point:
    def __init__(self, x, y):
        self._x, self._y = x,y
    def  __repr__(self):
        return f'({self._x}, {self._y})'

class Circle:
    def __init__(self, radius , center):
        self._radius = radius
        self._center = center
    def __repr__(self):
        return f'{self._center}, r = {self._radius}'
