from collections import UserList
class DefaultList(UserList):
    def __init__(self, _iterable=[], default=None):
        super().__init__(_iterable)
        self._default = default
    def __getitem__(self, index):
        try:
            return self.data[index]
        except:
            return self._default
