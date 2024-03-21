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
            self.data[:] = self._backup_data
        return True


# TEST_5:
numbers = {1, 2, 3, 4, 5}

with Atomic(numbers) as atomic:
    atomic.add(6)
    atomic.append(7)           # добавление элемента с помощью несуществующего метода

print(sorted(numbers))

with Atomic(numbers) as atomic:
    atomic.add(6)

print(sorted(numbers))