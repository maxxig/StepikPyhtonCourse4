from collections import UserString
class MutableString(UserString):
    def lower(self):
        # _change = self.data.lower()
        self.data = self.data.lower()
    def upper(self):
        self.data = self.data.upper()
    def sort(self, key=None, reverse=None):
        if key is not None:
            self.data =MutableString(''.join(map(lambda x: str(x),sorted([str(s) for s in self], key = key, reverse = reverse))))
        else:
            self.data = MutableString(
                ''.join(map(lambda x: str(x), sorted([str(s) for s in self]))))
        # _t = sorted(self, key = k, reverse = r)
        # self.data = ''.join(sorted(self, key = k, reverse = r))
    def __setitem__(self, key, value):
        if isinstance(key, slice):
            l = [item for item in self.data]
            l[key] = value
            self.data = ''.join(l)
        else:
            if key < 0 :
                while(key < 0):
                    key += len(self.data)
            self.data = self.data[:key] + value + self.data[key + 1:]
    # self._string = ''.join((map(lambda x: x if self._string.index(x) != key else value, self._string)))

    def __delitem__(self, key):
        if isinstance(key, slice):
            l = [item for item in self.data]
            del l[key]
            self.data = ''.join(l)
        else:
            l = [x for x in self.data]
            del l[key]
            self.data = ''.join(l)

