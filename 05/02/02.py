class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __repr__(self):
        return f'Rectangle(length={self.length}, width={self.width})'

# TEST_3:
figures = [Rectangle(1, 2), Rectangle(3, 4)]

print(figures)

# TEST_4:
array = [(80, 56), (77, 22), (28, 78), (33, 75), (47, 30), (79, 60), (47, 69), (26, 27), (39, 48), (64, 36)]
for length, width in array:
    rectangle = Rectangle(length, width)
    print(rectangle, repr(rectangle), sep='\n', end='\n\n')