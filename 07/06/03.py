def get_method_owner(cls, method):
    for _cls in cls.mro():
        if method in _cls.__dict__:
            return _cls
    else:
        return None