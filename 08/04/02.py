import functools
class MaxCallsException(Exception):
    pass

class limited_calls:
    def __init__(self, n):
        self.n = n
        self.counter = 0
    def __call__(self, func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self.counter >= self.n:
                raise MaxCallsException('Превышено допустимое количество вызовов')
            value = func(*args, **kwargs)
            self.counter += 1
            return value
        return wrapper




# TEST_4:
@limited_calls(10)
def power(a, n):
    return a ** n


for _ in range(10):
    power(2, 3)

try:
    print(power(2, 3))
except MaxCallsException as e:
    print(e)

# TEST_5:
@limited_calls(10)
def power(a, n):
    """degree"""
    return a ** n


print(power.__name__)
print(power.__doc__)
print(power(2, 3))