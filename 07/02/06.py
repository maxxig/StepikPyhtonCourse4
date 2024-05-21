class FieldTracker:
    fields = None
    def __init__(self):
        self._values = {}
        for f in self.fields:
            self._values[f] = self.__dict__[f]
    def base(self, attr):
        return self._values[attr]
    def has_changed(self, attr):
        if self.__dict__[attr] == self._values[attr]:
            return False
        return True
    def changed(self):
        return dict(filter(lambda x: self._values[x[0]] != self.__dict__[x[0]], self._values.items()))
    def save(self):
        for k,v in self._values.items():
            self._values[k] = self.__dict__[k]
