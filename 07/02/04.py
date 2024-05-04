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
class DoubledCounter(Counter):
    def inc(self, n = None):
        if n is None:
            super().inc(2)
        else:
            super().inc(n)
            super().inc(n)
    def dec(self, n = None):
        if n is None:
            super().dec(2)
        else:
            super().dec(n)
            super().dec(n)
