class PiggyBank:
    def __init__(self, coins):
        self.coins = coins

    def __repr__(self):
        return f'PiggyBank({self.coins})'

    def __mul__(self, other):
        print('22')
        return PiggyBank(self.coins * other)

    def __imul__(self, other):
        print('11')
        self.coins *= other


bank = PiggyBank(10)
print('1')
bank *= 5
print('e')
print(bank)