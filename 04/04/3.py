class User:
    @classmethod
    def check_age(cls, age):
        if type(age) != int or not 0 <= age <= 100:
            raise ValueError('Некорректный возраст')
        else:
            return True
    @classmethod
    def check_name(cls, name):
        if type(name) != str or  not name.isalpha():
            raise ValueError('Некорректное имя')
        else:
            return True
    def __init__(self, name, age):
        if self.check_name(name):
            self._name = name
        if self.check_age(age):
            self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        if self.check_name(name):
            self._name = name

    def get_age(self):
        return self._age

    def  set_age(self, age):
        if self.check_age(age):
            self._age = age


try:
    user = User('Gvido_1956', '67')
except ValueError as e:
    print(e)