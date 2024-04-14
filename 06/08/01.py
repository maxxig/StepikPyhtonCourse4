from keyword import kwlist
class NonKeyword:
    def __init__(self, attr):
        self._attr = attr
    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError("Атрибут не найден")
    def __set__(self, obj, value):
        if value not in kwlist:
            obj.__dict__[self._attr] = value
        else:
            raise ValueError("Некорректное значение")
    def __delete__(self, obj):
        del obj.__dict__[self._attr]
