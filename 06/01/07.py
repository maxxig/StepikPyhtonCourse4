from itertools import tee
class LoopTracker:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.iterable, self._first_iterator = tee(self.iterable)
        self._len = len(iterable)
        self._accesses = 0
        self._empty_accesses = 0
        try:
            self._first = next(self._first_iterator)
        except StopIteration as e:
            pass
        del self._first_iterator
    def __iter__(self):
        return self
    def __next__(self):
        try:
            res = next(self.iterable)
            self._last = res
            self._accesses += 1
            if '_first' not in self.__dict__:
                self._first = res
        except StopIteration:
            self._empty_accesses += 1
            raise
        return res
    @property
    def accesses(self):
        return self._accesses
    @property
    def empty_accesses(self):
        return self._empty_accesses
    @property
    def first(self):
        if '_first' in self.__dict__:
            return self._first
        else:
            raise AttributeError('Исходный итерируемый объект пуст')

    @property
    def last(self):
        if '_last' in self.__dict__:
            return self._last
        else:
            raise AttributeError('Последнего элемента нет')
    def is_empty(self):
        return True if self._len == self._accesses else False


# INPUT DATA:

# TEST_1:
loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(list(loop_tracker))

# TEST_2:
loop_tracker = LoopTracker([1, 2, 3])

print(loop_tracker.accesses)
next(loop_tracker)
next(loop_tracker)
print(loop_tracker.accesses)

# TEST_3:
loop_tracker = LoopTracker([1, 2, 3])
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

# TEST_4:
loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(loop_tracker.last)

print(next(loop_tracker))
print(loop_tracker.last)

print(next(loop_tracker))
print(loop_tracker.last)

# TEST_5:
loop_tracker = LoopTracker([1, 2])

print(loop_tracker.empty_accesses)
next(loop_tracker)
next(loop_tracker)

for _ in range(5):
    try:
        next(loop_tracker)
    except StopIteration:
        pass

print(loop_tracker.empty_accesses)

# TEST_6:
loop_tracker = LoopTracker([1, 2])

print(loop_tracker.is_empty())
next(loop_tracker)
print(loop_tracker.is_empty())
next(loop_tracker)
print(loop_tracker.is_empty())

# TEST_7:
loop_tracker = LoopTracker([1, 2, 3])

print(loop_tracker.first)
print(next(loop_tracker))

# TEST_8:
loop_tracker = LoopTracker([])

try:
    print(loop_tracker.first)
except AttributeError as e:
    print(e)

# TEST_9:
loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(loop_tracker.last)
print(next(loop_tracker))
print(loop_tracker.last)

# TEST_10:
loop_tracker = LoopTracker([1, 2, 3])

try:
    print(loop_tracker.last)
except AttributeError as e:
    print(e)

# TEST_11:
loop_tracker = LoopTracker(range(1_000))

for _ in range(100_000):
    next(loop_tracker, None)

print(loop_tracker.accesses)
print(loop_tracker.empty_accesses)

# TEST_12:
loop_tracker = LoopTracker(dict.fromkeys(range(100)))

print(next(loop_tracker))
print(next(loop_tracker))
print(next(loop_tracker))
print(loop_tracker.accesses)
print(loop_tracker.first)
print(loop_tracker.last)
print(loop_tracker.is_empty())

# TEST_13:
loop_tracker = LoopTracker([1, 2, 3])

try:
    loop_tracker.accesses = 1
except AttributeError as e:
    print(type(e))

try:
    loop_tracker.first = 1
except AttributeError as e:
    print(type(e))

try:
    loop_tracker.last = 1
except AttributeError as e:
    print(type(e))