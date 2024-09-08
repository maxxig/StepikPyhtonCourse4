class Stat:
    def __init__(self, iterable = []):
        self._iterable = iterable
    def add(self, value):
        self._iterable.append(value)
    def result(self):
        pass
    def clear(self):
        self._iterable.clear()

class MinStat(Stat):
    def result(self):
        if len(self._iterable) == 0:
            return None
        else:
            return min(self._iterable)
class MaxStat(Stat):
    def result(self):
        if len(self._iterable) == 0:
            return None
        else:
            return max(self._iterable)
class AverageStat(Stat):
    def result(self):
        if len(self._iterable) == 0:
            return None
        else:
            return sum(self._iterable)/len(self._iterable)