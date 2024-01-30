class SkipIterator:

    @classmethod
    def sta (cls, iterable, n):
        i, res = 0, []
        for o in iterable:
            if i == 0:
                res.append(o)
                i = n
            else:
                i-=1
                continue
        return res
    def __init__(self, iterable, n):
        self.res = iter(SkipIterator.sta(iterable, n))
    def __iter__(self):
        return self
    def __next__(self):
        return next(self.res)


# TEST_8:
skipiterator = SkipIterator(iter(['aa', 'bb', 'cc', 'dd', 'ee', 'ff']), 2)

print(*skipiterator)

# TEST_9:
data = ['к', 'б', 'ш', 'к', 'к', 'о', 'т', 'г', 'о', 'д', 'р', 'в', 'с', 'с', 'и', 'о', 'в', 'п', 'у', 'с', 'л', 'т',
        'г', 'т', 'з', 'ь', 'о', 'п', 'н', 'в', 'и', 'н', 'с', 'п', 'р', 'ш', 'е', 'к', 'н', 'с', 'у', 'в', 'п', 'т',
        'х', 'т', 'с', 'с', 'л', 'с']
skipiterator = SkipIterator(iter(data), 4)

print(*skipiterator)

# TEST_10:
skipiterator = SkipIterator(range(1000), 7)

for _ in range(25):
    next(skipiterator)

print(next(skipiterator))
print(next(skipiterator))
print(next(skipiterator))

