class SortKey:
    def __init__(self, *args):
        self.args = args
    def __call__(self, obj):
        # print(tuple(obj.__dict__[i] for i in self.args))
        # print('s')
        return tuple(obj.__dict__[i] for i in self.args)

# TEST_5:
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'

users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

users.sort(key=SortKey('name'), reverse=True)
print(users)
users.sort(key=SortKey('name', 'age'), reverse=True)
print(users)
users.sort(key=SortKey('age'), reverse=True)
print(users)
users.sort(key=SortKey('age', 'name'), reverse=True)