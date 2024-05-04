class Versioned:
    def __set_name__(self, cls, attr):
        self._attr = attr
    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError("Атрибут не найден")
    def __set__(self, obj, value):
        if '_values' not in obj.__dict__:
            obj._values = []
            obj._values.append(value)
        else:
            obj._values.append(value)
        obj.__dict__[self._attr] = value

    def get_version(self, obj, n):
        return obj._values[n-1]

    def set_version(self, obj, value):
        obj.__dict__[self._attr] = obj._values[value-1]


# TEST_8:
class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19
student.age = 20

print(student.age)

Student.age.set_version(student, 1)

print(student.age)
for i in range(3):
    print(Student.age.get_version(student, i + 1))

Student.age.set_version(student, 2)

print(student.age)
for i in range(3):
    print(Student.age.get_version(student, i + 1))

# TEST_9:
class Student:
    age = Versioned()

print(Student.age.__class__)