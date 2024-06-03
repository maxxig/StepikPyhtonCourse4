from collections.abc import Sequence
class CustomRange(Sequence):
    def __init__(self, *args):
        self._values = []
        for a in args:
            try:
                _res = int(a)
                self._values.append(_res)
                continue
            except:
                pass
            if '-' in a:
                _start,_stop = a.split('-')
                for t in range(int(_start),int(_stop)+1):
                    self._values.append(t)
    def __getitem__(self, item):
        return self._values[item]
    def __len__(self):
        return len(self._values)




# TEST_6:
customrange = CustomRange(1, 212, '89-323', 87, '17-82', 124, '300-312', 832, 1234)

print(*customrange)
print(customrange[11])
print(customrange[44])
print(customrange[-12])
print(customrange[-38])
print(82 in customrange)
print(17 in customrange)