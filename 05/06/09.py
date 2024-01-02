class CachedFunction:
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args, **kwargs):
        # t = (args,)
        if args in self.cache:
            return self.cache[args]
        else:
            res = self.func(*args, **kwargs)
            self.cache[args] = res
            return res


# TEST_5:
@CachedFunction
def tribonacci(n):
    if n in (1, 2, 3):
        return 1
    return tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1)


print(tribonacci(200))
print(len(tribonacci.cache))