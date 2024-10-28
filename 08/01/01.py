from functools import total_ordering

@total_ordering
class Shape:
    __slots__ = ('name', 'color', 'area')
    def __init__(self, name, color, area):
        self.name = name
        self.color = color
        self.area = area
    def __repr__(self):
        return f'{self.color} {self.name} ({self.area})'
    def __eq__(self, other):
        if isinstance(other, Shape):
            return self.area == other.area
        else:
            return NotImplemented
    def __lt__(self, other):
        if isinstance(other, Shape):
            return self.area < other.area
        else:
            return NotImplemented

# TEST_10:
shape = Shape('square', 'LemonChiffon', 50)

print(shape.__eq__(1))
print(shape.__ne__(1.1))
print(shape.__gt__(range(5)))
print(shape.__lt__([1, 2, 3]))
print(shape.__ge__({4, 5, 6}))
print(shape.__le__({1: 'one'}))
