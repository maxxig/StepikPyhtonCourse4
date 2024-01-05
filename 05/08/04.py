class DefaultObject:
    def __init__(self, default = None, **kwargs):
        self.default = default
        for key, value in kwargs.items():
            super().__setattr__(key, value)
    def __getattr__(self, item):
        return self.default

# TEST_4:
god = DefaultObject(name='Kratos', mythology='greek')
print('name' in god.__dict__)
print('mythology' in god.__dict__)