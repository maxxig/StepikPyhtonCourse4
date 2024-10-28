import inspect, re
def snake_case(attrs=False):
    def decorator(cls):
        func_list = [m[0] for m in inspect.getmembers(cls, predicate=inspect.isfunction) if not m[0].startswith('__')]
        for f in func_list:
            if f.startswith('_'):
                new_name = '_' + re.sub(r'(?<!^)(?=[A-Z])', '_', f[1:]).lower()
            else:
                new_name = re.sub(r'(?<!^)(?=[A-Z])', '_', f).lower()
            setattr(cls, new_name,cls.__dict__[f])
            delattr(cls,f)
        if attrs:
            attr_list = [attr for attr in dir(cls) if not attr.startswith('__')]
            for attr in attr_list:
                new_name = re.sub(r'(?<!^)(?=[A-Z])', '_', attr).lower()
                setattr(cls, new_name, cls.__dict__[attr])
                delattr(cls, attr)
        return cls

    return decorator