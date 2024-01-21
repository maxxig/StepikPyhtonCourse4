class Row:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            super().__setattr__(k, v)
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError("Изменение значения атрибута невозможно")
        else:
            raise AttributeError("Установка нового атрибута невозможна")
    def __delattr__(self, name):
        raise AttributeError("Удаление атрибута невозможно")

    def __repr__(self):
        return 'Row('+', '.join([f'{k}={repr(v)}' for k, v in self.__dict__.items()])+')'

    def __eq__(self, other):
        if isinstance(other, Row):
            return tuple(self.__dict__.items()) == tuple(other.__dict__.items())
        else:
            return NotImplemented

    def __hash__(self):
        return hash(tuple(self.__dict__.items()))

# TEST_8:
row = Row(a=16, b=100, country='Jamaica')
print(row.__eq__(1))
print(row.__ne__(1.1))

# TEST_9:
row1 = Row(a=1, b=2, c=3)
row2 = Row(a=3, b=2, c=1)
print(row1 == row2)

# TEST_10:
row1 = Row(a=1, b=2, c=3)
row2 = Row(b=1, a=2, c=3)

print(row1 == row2)
print(hash(row1) == hash(row2))