class Queue:
    def __init__(self, *args):
        self.items = []
        self.items.extend(args)
    def add(self, *args):
        self.items.extend(args)
    def pop(self):
        return self.items.pop(0) if self.items else None
    def __add__(self, other):
        # print('123')
        if isinstance(other, Queue):
            res = self.items.copy()
            res.extend(other.items)
            return Queue(*res)
        else:
            return NotImplemented

    def __str__(self):
        # print('s')
        return ' -> '.join([str(s) for s in self.items])

    def __eq__(self, other):
        if isinstance(other, Queue):
            res = True
            if len(self.items) != len(other.items):
                return False
            for i in range(len(self.items)):
                if self.items[i] != other.items[i]:
                    res = False
            return res
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Queue):
            self.items.extend(other.items)
            return self
        else:
            return NotImplemented
    def __rshift__(self, n):
        if isinstance(n, int):
            if n >= len(self.items):
                return Queue()
            else:
                return Queue(*self.items[n:])
        return NotImplemented




# TEST_10:
queue = Queue(1, 2, 3)
print(queue.__add__([]))
print(queue.__iadd__('bee'))
print(queue.__rshift__('geek'))