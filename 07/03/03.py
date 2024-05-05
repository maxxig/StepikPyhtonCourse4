class FuzzyString(str):
    def __new__(cls, value):
        instance = super().__new__(cls, value)
        return instance
    def __eq__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        else:
            return self.lower() == other.lower()
    def __ne__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        else:
            return self.lower() != other.lower()
    def __contains__(self, item):
        return item.lower() in self.lower()
    def __ge__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        else:
            return self.lower() >= other.lower()
    def __le__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        else:
            return self.lower() <= other.lower()
    def __gt__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        else:
            return self.lower() > other.lower()
    def __lt__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        else:
            return self.lower() < other.lower()