from abc import ABC, abstractmethod
class Validator(ABC):
    def __set_name__(self, cls, attr):
        self._attr = attr
    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError("Атрибут не найден")
    def __set__(self, obj, value):
        self.validate(value)
        obj.__dict__[self._attr] = value
    def __delete__(self, obj):
        del obj.__dict__[self._attr]
    @abstractmethod
    def validate(self, obj):
        pass

class Number(Validator):
    def __init__(self, minvalue = None, maxvalue = None):
        self._minvalue, self._maxvalue = minvalue , maxvalue
    def validate(self, obj):
        if not isinstance(obj, int|float):
            raise TypeError("Устанавливаемое значение должно быть числом")
        elif self._minvalue is not None and obj < self._minvalue:
            raise ValueError(f"Устанавливаемое число должно быть больше или равно {self._minvalue}")
        elif self._maxvalue is not None and obj > self._maxvalue:
            raise ValueError(f"Устанавливаемое число должно быть меньше или равно {self._maxvalue}")
class String(Validator):
    def __init__(self, minsize = None, maxsize = None, predicate = None):
        self._minsize, self._maxsize, self._predicate = minsize, maxsize, predicate
    def validate(self, obj):
        if not isinstance(obj, str):
            raise TypeError("Устанавливаемое значение должно быть строкой")
        elif self._minsize is not None and len(obj) < self._minsize:
            raise ValueError(f"Длина устанавливаемой строки должна быть больше или равна {self._minsize}")
        elif self._maxsize is not None and len(obj) > self._maxsize:
            raise ValueError(f"Длина устанавливаемой строки должна быть меньше или равна {self._maxsize}")
        elif self._predicate is not None and self._predicate(obj) == False:
            raise ValueError(f"Устанавливаемая строка не удовлетворяет дополнительным условиям")