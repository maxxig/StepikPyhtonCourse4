import random
class Dice:
    def __init__(self, sides=6):
        self.sides = sides
    def __call__(self):
        tmp = list(range(1, self.sides+1))
        s = random.randint(1, self.sides)
        # print(tmp, s)
        return tmp[s-1]


# TEST_5:
kingdice = Dice(20)
print(callable(kingdice))