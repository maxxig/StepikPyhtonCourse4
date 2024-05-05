class RoundedInt(int):
    def __new__(cls, num, even=True):
        e = num % 2
        if e == 0 and not even:
            num += 1
        elif e == 1 and even:
            num +=1
        instance = super().__new__(cls, num)
        return instance

# TEST_5:
for digit in range(100):
    print(RoundedInt(digit, False))