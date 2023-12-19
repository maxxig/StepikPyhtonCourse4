class Pet:
    _first = None
    _last = None
    _cnt = 0
    def __init__(self, name):
        self.name = name
        self._cnt += 1
        if self._first == None:
            self.set_first(self)
        else:
            self.set_last(self)

    @classmethod
    def set_first(cls, c):
        cls._first = c
        cls._last = c
        cls._cnt += 1
    @classmethod
    def set_last(cls, c):
        cls._last = c
        cls._cnt += 1
    @classmethod
    def first_pet(cls):
        return cls._first

    @classmethod
    def last_pet(cls):
        return cls._last

    @classmethod
    def num_of_pets(cls):
        return cls._cnt


# TEST_5:
pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')
pet4 = Pet('Ratchet')
pet5 = Pet('Ratchet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())



