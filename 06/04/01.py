def is_context_manager(obj):
    if '__enter__' in dir(obj) and '__exit__' in dir(obj):
        return True
    return False


# TEST_2:
from tempfile import TemporaryFile

with TemporaryFile(mode='r+') as file:
    print(is_context_manager(file))

# TEST_3:
from threading import Lock

print(is_context_manager(Lock()))

# TEST_4:
print(is_context_manager(1992))
print(is_context_manager('beegeek'))
print(is_context_manager([1, 2, 3]))
print(is_context_manager({'one': 1, 'two': 2}))
print(is_context_manager(None))


# TEST_5:
class ContextManager:
    def __enter__(self):
        return 'beegeek'

    def __exit__(self, exc_type, exc_value, exc_tb):
        return True


print(is_context_manager(ContextManager()))


# TEST_6:
class ContextManager:
    def __init__(self):
        self.inside = False

    def __enter__(self):
        self.inside = True
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.inside = False
        return True


print(is_context_manager(ContextManager()))


# TEST_7:
class ContextManager:
    def __enter__(self):
        return 'beegeek'


print(is_context_manager(ContextManager()))


# TEST_8:
class ContextManager:
    def __init__(self):
        self.inside = False

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.inside = False
        return True


print(is_context_manager(ContextManager()))