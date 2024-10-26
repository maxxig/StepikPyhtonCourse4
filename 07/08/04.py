class Queue:
    def __init__(self, pairs=[]):
        self._pairs = {}
        if isinstance(pairs, dict):
            for key, value in pairs.items():
                self._pairs[key] =value
        elif isinstance(pairs, list):
            for item in pairs:
                self._pairs[item[0]] = item[1]
    def add(self, item):
        if item[0] in self._pairs.keys():
            del self._pairs[item[0]]
        self._pairs[item[0]] = item[1]
    def pop(self):
        if len(self._pairs) == 0:
            raise KeyError("Очередь пуста")
        else:
            item = next(iter(self._pairs))
            res = (item, self._pairs.pop(item))
            return res
    def __str__(self):
        return'Queue([' + ', '.join([f'''('{k}', {v})''' for k,v in self._pairs.items()]) +'])'

    def __len__(self):
        return len(self._pairs)

queue = Queue()

queue.add(('one', 1))
queue.add(('two', 2))
print(queue)