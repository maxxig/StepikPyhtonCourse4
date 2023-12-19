from functools import singledispatchmethod
class Processor:
    @singledispatchmethod
    @classmethod
    def process(self, data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    @process.register(int)
    @process.register(float)
    @classmethod
    def int_float_process(self, data):
        return data * 2

    @process.register(tuple)
    @classmethod
    def tuple_process(self, data):
        return tuple(sorted(data))
    @process.register(list)
    @classmethod
    def tuple_process(self, data):
        return sorted(data)
    @process.register(str)
    @classmethod
    def str_process(self, data):
        return data.upper()

objects = [None, {1, 2, 3}, {1: 'one', 2: 'two'}]

for obj in objects:
    try:
        Processor.process(obj)
    except TypeError as e:
        print(e)