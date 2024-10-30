def auto_repr(args, kwargs):
    def decorator(cls):
        nonlocal args
        nonlocal kwargs
        setattr(cls, '_args', args)
        setattr(cls, '_kwargs', kwargs)
        def my_repr(self):
            res = f'{self.__class__.__name__}('
            if len(args)>0:
                res += ", ".join([repr(getattr(self, a)) for a in getattr(self,'_args')])
            if len(args)>0 and len(kwargs)>0:
                res += ', '
            if len(kwargs)>0:
                res += ", ".join([f"{a}={repr(getattr(self, a))}" for a in getattr(self, '_kwargs')])
            res += ')'
            return res
        setattr(cls, '__repr__', my_repr)
        return cls
    return decorator





# TEST_5:
@auto_repr(args=['x', 'y'], kwargs=['color'])
class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

point = Point(1, 2, color='green')
print(repr(point))

point.x = 10
point.y = 20
print(repr(point))