class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    @classmethod
    def square(cls, side):
         return Rectangle(side, side)


# TEST_3:
array = [416, 347, 228, 276, 159, 54, 302, 256, 355, 57, 370, 309, 455, 242, 345, 90, 413, 77, 143, 494, 397, 380, 477, 391, 139, 421, 367, 275, 397, 181]

for side in array:
    rectangle = Rectangle.square(side)
    print(rectangle.length == rectangle.width)

# TEST_4:
array = [(99, 297), (215, 472), (270, 80), (453, 215), (333, 360), (52, 426), (307, 257), (425, 493), (291, 437), (57, 415)]


for length, width in array:
    rectangle = Rectangle(length, width)
    print(f'Длина = {rectangle.length}, Ширина = {rectangle.width}')

# TEST_5:
rectangle = Rectangle(1, 2)
print(hasattr(rectangle, 'length'))
print(hasattr(rectangle, 'width'))