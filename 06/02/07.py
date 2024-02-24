import copy
class PermaDict:
    def __init__(self, data = {}):
        self._data = copy.deepcopy(data)
    def keys(self):
        return self._data.keys()
    def values(self):
        return self._data.values()
    def items(self):
        return [(k, v) for k, v in self._data.items()]
    def __iter__(self):
        return iter(self._data.keys())
    def __len__(self):
        return len(self._data)

    def __getitem__(self, key):
        return self._data[key]
    def __setitem__(self, key, value):
        if key not in self._data:
            self._data[key] = value
        else:
            raise KeyError('Изменение значения по ключу невозможно')
    def __delitem__(self, key):
        del self._data[key]


# TEST_7:
permadict = PermaDict()
print('Keys:', *permadict.keys())
print('Values:', *permadict.values())
print('Items:', *permadict.items())