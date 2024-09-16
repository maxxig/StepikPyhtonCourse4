import functools
class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        res = True
        for arg in args:
            if not isinstance(arg, int|float):
                res = False
                break
        for kw in kwargs.values():
            if not isinstance(kw, int|float):
                res = False
                break
        if res:
            return self.func(*args, **kwargs)
        else:
            raise TypeError('Аргументы должны принадлежать типам int или float')