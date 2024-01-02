class RaiseTo:
    def __init__(self, degree):
        self.degree = degree
    def __call__(self, x):
        return x ** self.degree


raise_to_zero = RaiseTo(0)
raise_to_negativ = RaiseTo(-1)
digits = [124, 215, 515, 2353654, 1247, 54, 2145, 925, 245, 2156, 26]

for digit in digits:
    print(raise_to_zero(digit), raise_to_negativ(digit), sep='; ')