class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 0
    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)

# TEST_6:
@CountCalls
def add(a, b):
    return a + b

@CountCalls
def mul(a, b):
    return a * b

print(add(1, 2))
print(add(3, 4))
print(mul(5, 6))

print(add.calls)
print(mul.calls)
