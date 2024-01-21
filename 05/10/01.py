class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def color(self):
        return self._color

    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return self._x == other._x and self._y == other._y and self._color == other._color
        else:
            return NotImplemented
    def __hash__(self):
        return hash((self._x, self._y, self._color))

    def __repr__(self):
        return f"ColoredPoint({self._x}, {self._y}, '{self._color}')"

coloredpoint = ColoredPoint(1, 2, 'yellow')

try:
    coloredpoint.x = 2
except AttributeError as e:
    print(type(e))

try:
    coloredpoint.y = 3
except AttributeError as e:
    print(type(e))

try:
    coloredpoint.color = 'black'
except AttributeError as e:
    print(type(e))