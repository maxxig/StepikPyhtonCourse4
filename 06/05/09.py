import copy
class Atomic:
    def __init__(self, data, deep=False):
        self.data = data
        self.deep = deep

    def __enter__(self):
        if self.deep:
            self._backup_data = copy.deepcopy(self.data)
        else:
            self._backup_data = copy.copy(self.data)
        return self._backup_data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            if isinstance(self.data, list):
                self.data[:] = self._backup_data
            elif isinstance(self.data, dict|set):
                self.data.clear()
                self.data.update(self._backup_data)
        return True


# TEST_7:
data = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}

with Atomic(data) as atomic:
    atomic['e'] += 2   # изменение структуры

print(data)

# TEST_8:
matrix = [[1, 2], [3, 4]]

with Atomic(matrix, True) as atomic:
    atomic[1].append(0)

print(matrix)