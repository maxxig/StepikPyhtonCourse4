class AttrsIterator:
    def __init__(self, obj):
        self.obj = obj
        self.return_val = iter(obj.__dict__.items())
    def __iter__(self):
        return self

    def __next__(self):
        return next(self.return_val)


# TEST_4:
class Kish:
    def __init__(self, song, year):
        self.song = song
        self.year = year


forester = Kish('лесник', 1997)
attrs_iterator = AttrsIterator(forester)

next(attrs_iterator)
next(attrs_iterator)

try:
    next(attrs_iterator)
except StopIteration:
    print('Атрибуты закончились')
