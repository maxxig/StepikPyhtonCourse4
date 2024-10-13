import functools
class ignore_exception:
    def __init__(self, *args):
        self.args = args

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                value = func(*args, **kwargs)
                return value
            except Exception as e:
                if type(e) in self.args:
                    print(f"Исключение {type(e).__name__} обработано")
                else:
                    raise type(e)
        return wrapper