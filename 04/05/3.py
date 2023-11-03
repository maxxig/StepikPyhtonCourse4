class Person:
    def __init__(self, name, surname):
        self.name, self.surname = name, surname

    def get_fullname (self):
        return f'{self.name} {self.surname}'

    def set_fullname(self, fullname):
        self.name = fullname.split()[0]
        self.surname = fullname.split()[1]

    fullname = property(get_fullname, set_fullname)


person = Person('Брайан', 'Керниган')
print(hasattr(person, 'name'))
print(hasattr(person, 'surname'))
print(hasattr(person, 'fullname'))
