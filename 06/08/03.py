class MaxCallsException(Exception):
    pass
class LimitedTakes:
    def __init__(self, times):
        self._times = times
    def __set_name__(self, cls, attr):
        self._attr = attr
        self._counter = 0
    def __get__(self, obj, cls):
        if self._counter >= self._times:
            raise MaxCallsException("Превышено количество доступных обращений")
        if obj is None:
            self._counter += 1
            return self
        if self._attr in obj.__dict__:
            self._counter += 1
            return obj.__dict__[self._attr]
        else:
            raise AttributeError("Атрибут не найден")
    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value
