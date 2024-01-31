class RandomLooper:
    def __init__(self, *args):
        self.arg = iter([a for arg in args for a in arg])
    def __iter__(self):
        return self
    def __next__(self):
        return next(self.arg)

# TEST_4:
randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'])

answer = [next(randomlooper) for _ in range(4)]
print(answer)