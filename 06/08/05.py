import random
class RandomNumber:
    def __init__(self, start, end, cache = False):
        self._start, self._end, self._cache = start, end, cache
        self._cached_number = None
    def __set_name(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._cache and self._cached_number is not None:
            return self._cached_number
        number = random.randint(self._start, self._end)
        if self._cache:
            self._cached_number = number
        return number
    def __set__(self, obj, value):
        raise AttributeError("Изменение невозможно")


class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)

print(MagicPoint.x.__class__)
print(MagicPoint.y.__class__)
print(MagicPoint.z.__class__)