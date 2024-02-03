class CyclicList:
    def __init__(self, iterable=[]):
        self.iterable = list(iterable)

    def append(self, item):
        self.iterable.append(item)

    def pop(self, index=None):
        if index is None:
            return self.iterable.pop()
        else:
            return self.iterable.pop(index)
    def __len__(self):
        return len(self.iterable)

    def __getitem__(self, index):
        _index = index % len(self.iterable)
        return self.iterable[_index]



# TEST_7:
cyclic_list = CyclicList()
cyclic_list.append(1)

for index, elem in enumerate(cyclic_list):
    if index > 6:
        break
    print(elem, end=' ')