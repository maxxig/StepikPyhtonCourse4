import copy
class AttrDict:
    def __init__(self, data = {}):
        self._data = copy.deepcopy(data)
        for d in self._data:
            if isinstance(d, str):
                setattr(self, d, self._data[d])
    def __getitem__(self, item):
        return self._data[item]

    def __len__(self):
        return len(self._data)

    def __setitem__(self, key, value):
        self._data[key] = value
        if isinstance(key, str):
            setattr(self, key, value)

    def __iter__(self):
        return iter(self._data)




# TEST_2:
attrdict = AttrDict({'name': 'Timur', 'city': 'Moscow'})

attrdict['city'] = 'Dubai'
attrdict['age'] = 31
print(attrdict.city)
print(attrdict.age)

# TEST_3:
attrdict = AttrDict()

attrdict['school_name'] = 'BEEGEEK'
print(attrdict['school_name'])
print(attrdict.school_name)

# TEST_4:
d = AttrDict()
d.name = 'Leonardo da Vinci'

try:
    print(d['name'])
except KeyError:
    print('Ключ отсутствует')

# TEST_5:
d = dict.fromkeys(range(100), None)
attrdict = AttrDict(d)
print(*attrdict)

d[100] = None
print(*attrdict)