class Summator:
    mult = 1
    def total(self, n):
        arr = map(lambda x: x ** self.mult, range(1,n + 1))
        return sum(arr)
class SquareSummator(Summator):
    mult = 2
class QubeSummator(Summator):
    mult = 3
class CustomSummator(Summator):
    def __init__(self, m):
        self.mult = m