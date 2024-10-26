import functools
def singleton(ori_cls):
    old_new = ori_cls.__new__
    instance = None

    @functools.wraps(old_new)
    def new_new(cls, *args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = old_new(cls)
        return instance

    ori_cls.__new__ = new_new
    return ori_cls