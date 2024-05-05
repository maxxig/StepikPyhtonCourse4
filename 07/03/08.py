import copy
class ModularTuple(tuple):
    def __new__(cls, iterable = None, size=100):
        _iter = copy.deepcopy(iterable)
        if _iter:
            _iter = tuple(map(lambda x: x % size, _iter))
        else:
            _iter = tuple()
        return super().__new__(cls, tuple(_iter))