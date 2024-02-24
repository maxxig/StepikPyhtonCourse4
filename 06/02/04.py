import copy
class SequenceZip:
    def __init__(self, *args):
        _args = copy.deepcopy(args)
        self.iterable = zip(*_args)
    def __len__(self):
        temp = copy.deepcopy(self.iterable)
        _len = 0
        while(1):
            try:
                next(temp)
                _len += 1
            except StopIteration:
                break
        return _len
    def __getitem__(self, key):
        temp = copy.deepcopy(self.iterable)
        res = None
        for i in range(key+1):
            res = next(temp)
        return res



# TEST_4:
x, y, z = [1, 2, 3], [4, 5, 6], [7, 8, 9]
sequencezip = SequenceZip(x, y, z)

print(sequencezip[2])
x[-1], z[-1] = z[-1], x[-1]
print(sequencezip[2])
