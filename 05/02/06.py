class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs
        # l = list(map(lambda x: f"{x[0]}='{x[1]}'" if isinstance(x[1], str) else f"{x[0]}={x[1]}", [(k, v) for k, v in self.__dict__.items()]))
        # print(l)
    def __repr__(self):
        test = ', '.join(list(map(lambda x: f"{x[0]}='{x[1]}'" if isinstance(x[1], str) else f"{x[0]}={x[1]}", [(k, v) for k, v in self.__dict__.items()])))
        return f"AnyClass({test})"
    def __str__(self):
        test = ', '.join(list(map(lambda x: f"{x[0]}='{x[1]}'" if isinstance(x[1], str) else f"{x[0]}={x[1]}", [(k, v) for k, v in self.__dict__.items()])))
        return f"AnyClass: {test}"


# TEST_5:
attrs = {
    'name': 'Margaret Heafield Hamilton',
    'birth_date': '17.09.1936',
    'age': 86,
    'career': 'computer scientist'
}
obj = AnyClass(**attrs)
print(obj)
