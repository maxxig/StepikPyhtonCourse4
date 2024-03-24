class Greeter:
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        print("Приветствую, " + self.name)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("До встречи, " + self.name)

# TEST_5:
with Greeter('Gvido') as greeter:
    try:
        print(greeter.age)
    except AttributeError as e:
        print(f'Атрибут "{e.name}" отсутствует')