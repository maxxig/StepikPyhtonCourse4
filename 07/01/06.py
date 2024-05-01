class Counter:
    def __init__(self, start =  0):
        self.value = start
    def inc(self, n = 1):
        self.value += n
    def dec(self, n = 1):
        if self.value - n < 0:
            self.value = 0
        else:
            self.value -= n
class NonDecCounter(Counter):
    def dec(self, *args, **kwargs):
        pass
class LimitedCounter(Counter):
    def __init__(self, start = 0, limit = 10):
        self.value = start
        self._limit = limit
    def inc(self, n = 1):
        if self.value + n <= self._limit:
            self.value += n
        else:
            self.value = self._limit
