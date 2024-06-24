from collections.abc import Sequence
import copy
class BitArray(Sequence):
    def __init__(self, iterable = None):
        if iterable is not None:
            temp = copy.deepcopy(iterable)
            self._values = temp
        else:
            self._values = []
    def __str__(self):
        return '[' + ', '.join([str(s) for s in self._values]) + ']'
    def __len__(self):
        return len(self._values)
    def __getitem__(self, item):
        return self._values[item]
    def __invert__(self):
        return  BitArray(list(map(lambda x: 1 if x == 0 else 0, self._values)))
    def __and__(self, other):
        try:
            return BitArray(list(map(lambda x: x[0] & x[1],zip(self._values, other, strict=True))))
        except:
            return NotImplemented
    def __or__(self, other):
        try:
            return BitArray(list(map(lambda x: x[0] | x[1],zip(self._values, other, strict=True))))
        except:
            return NotImplemented