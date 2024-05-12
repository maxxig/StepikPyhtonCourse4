class AdvancedList(list):
    def join(self, _splitter = ' '):
        return _splitter.join(map(lambda x: str(x),self))

    def map(self, _func):
        r = list(map(_func, self))
        super().__init__(r)

    def filter(self, _func):
        r = list(filter(_func, self))
        super().__init__(r)