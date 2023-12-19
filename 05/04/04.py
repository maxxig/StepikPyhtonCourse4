class ColoredPoint:
    def __init__(self, x, y, color = (0, 0, 0)):
        self.x, self.y, self.color = x, y, color
    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, {self.color})"
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __pos__(self):
        return ColoredPoint(self.x, self.y, self.color)

    def __neg__(self):
        return ColoredPoint(self.x * -1, self.y * -1, self.color)

    def __invert__(self):
        return ColoredPoint(self.y, self.x, (255 - self.color[0], 255 - self.color[1], 255 - self.color[2]))

point = ColoredPoint(0, 0, (0, 0, 0))

print(f'{+point}; {-point}; {~point}')
print(point.color)