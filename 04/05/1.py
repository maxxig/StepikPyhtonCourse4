class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return 2*self.length + 2*self.width
    perimeter = property(get_perimeter)

    def get_aree(self):
        return self.length * self.width

    area = property(get_aree)

rectangle = Rectangle(20, 20)
array = [(39, 48), (64, 36), (80, 56), (79, 60), (47, 30), (26, 27), (47, 69), (77, 22), (28, 78), (33, 75)]
for length, width in array:
    rectangle.length = length
    rectangle.width = width
    print(f'Периметр = {rectangle.perimeter}, Площадь = {rectangle.area}')