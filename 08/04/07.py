import functools
class type_check:
    def __init__(self, types: list):
        self.types = types

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for item in zip(args, self.types, strict=False):
                if not isinstance(item[0], item[1]):
                    raise TypeError()
            return func(*args, **kwargs)
        return wrapper

# TEST_5:
@type_check([])
def add(a, b):
    return a + b


print(add(1, 2))

# TEST_6:
@type_check([int, int, str])
def add(a, b, c=3):
    return a + b + c


print(add(1, 2, c=5))