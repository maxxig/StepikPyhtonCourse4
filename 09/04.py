class ArithmeticProgression:
    def __init__(self, start, step):
        self._current = start - step
        self._step = step
    def __iter__(self):
        return self

    def __next__(self):
        self._current += self._step
        return self._current

class GeometricProgression :
    def __init__(self, start, step):
        self._current = start/step
        self._step = step
    def __iter__(self):
        return self

    def __next__(self):
        self._current *= self._step
        return int(self._current)




# TEST_5:
progression = GeometricProgression(100, 10)
count = 0

for item in progression:
    if count == 20:
        break
    count += 1
    print(item, end=' ')