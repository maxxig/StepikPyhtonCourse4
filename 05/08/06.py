class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.attrs_num = 0
        for key, value in kwargs.items():
            setattr(self, key, value)
            # self.attrs_num += 1
    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        l = self.attrs_num + 1
        object.__setattr__(self, 'attrs_num', l)
    def __delattr__(self, item):
        super().__delattr__(item)
        self.__dict__['attrs_num'] -= 1

# TEST_5:
person = AttrsNumberObject(name='Mark')

print(person.attrs_num)

person.surname = 'Zuckerberg'
print(person.attrs_num)

person.age = 38
print(person.attrs_num)

person.job = 'Programmer'
print(person.attrs_num)
