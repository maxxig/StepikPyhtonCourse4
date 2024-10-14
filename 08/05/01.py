import functools

def track_instances(cls):
    old_init = cls.__init__

    @functools.wraps(old_init)
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        if hasattr(cls, 'instances'):
            cls.instances.append(self)
        else:
            cls.instances = [self]

    cls.__init__ = new_init
    return cls