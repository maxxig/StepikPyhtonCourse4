import copy
class HistoryDict:
    def __init__(self, data ={}):
        self._data = copy.deepcopy(data)
        self._history = {}
        for k, v in self._data.items():
            self.add_to_history(k, v)

    def add_to_history(self, key, value):
        if key not in self._history:
            self._history[key] = [value]
        else:
            self._history[key].append(value)
    def keys(self):
        return self._data.keys()
    def values(self):
        return self._data.values()
    def items(self):
        return [(k, v) for k, v in self._data.items()]
    def __len__(self):
        return len(self._data)
    def __setitem__(self, key, value):
        self._data[key] = value
        self.add_to_history(key, value)
    def __getitem__(self, key):
        return self._data.get(key)
    def __iter__(self):
        return iter(self._data)
    def __delitem__(self, key):
        del self._data[key]
        del self._history[key]
    def all_history(self):
        return self._history
    def history(self, key):
        if key in self._history:
            return self._history[key]
        return []

historydict = HistoryDict({'ducks': 99, 'cats': 1})

historydict['ducks'] = 100
print(historydict.history('ducks'))
print(historydict.history('cats'))
print(historydict.history('dogs'))
