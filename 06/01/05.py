from itertools import tee
class Peekable:
    def __init__(self, iterable ):
        self.iterable = iter(iterable)
    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterable)

    def peek(self, *args, **kwargs):
        self.iterable, temp_iter = tee(self.iterable)
        try:
            res = next(temp_iter)
        except StopIteration:
            if len(args)>0:
                return args[0]
            elif 'default' in kwargs.keys():
                return kwargs['default']
            else:
                raise StopIteration
        return res


# TEST_5:
from itertools import islice

iterator = Peekable([n ** 2 for n in [1, 2, 3, 4, 5]])

print(iterator.peek())
print(list(islice(iterator, 2)))

print(iterator.peek())
print(iterator.peek())

print(list(islice(iterator, 2)))
print(list(islice(iterator, 2)))

# TEST_6:
iterator = Peekable([n ** 2 for n in [1, 2, 3]])

print(iterator.peek(default=0))
print(*iterator)
print(iterator.peek(default=None))
print(iterator.peek(default=1))
print(iterator.peek(default=[]))
print(iterator.peek(default=()))