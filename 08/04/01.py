import functools
class reverse_args:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func                            # декорируемая функция

    def __call__(self, *args, **kwargs):
        value = self.func(*args[::-1], **kwargs)
        return value