import functools
def recviz(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        space = '    '
        param1 = ', '.join([repr(i) for i in args])
        param2 = ', '.join([f'{k}={repr(v)}' for (k,v) in kwargs.items()])
        params = ''
        if param1 and param2:
            params = param1 + ', '+ param2
        elif param1 and not param2:
            params = param1
        else:
            param2
        wrapper.num += 1
        print(f'{space * wrapper.num}-> {func.__name__}({params})')
        r = func(*args, **kwargs)
        print(f'{space * wrapper.num}<- {repr(r)}')
        wrapper.num -= 1
        return r

    wrapper.num = -1
    return wrapper


@recviz
def add(a, b, c, d, e):
    return (a + b + c) * (d + e)

add('a', b='b', c='c', d=3, e=True)