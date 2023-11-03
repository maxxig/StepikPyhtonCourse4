class ElectricCar:
    def __init__(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def del_color(self):
        del self._color

    color = property(get_color, set_color, del_color)


car = ElectricCar('black')

car.color = 'yellow'
car.color = 'white'

del car.color

print(car.color)