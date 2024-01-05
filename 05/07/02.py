class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature
    def to_fahrenheit(self):
        return self.temperature * 9 / 5 + 32
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celsius = 5/9 * (fahrenheit - 32)
        return Temperature(celsius)
    def __bool__(self):
        return True if self.temperature > 0 else False
    def __int__(self):
        return int(self.temperature)
    def __float__(self):
        return float(self.temperature)
    def __str__(self):
        return f'{round(self.temperature, 2)}°C'

t = Temperature.from_fahrenheit(132.7)
print(t)


