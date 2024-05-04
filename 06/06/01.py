from contextlib import contextmanager
@contextmanager
def make_tag(tag):
    print(tag)
    yield
    print(tag)

# TEST_2:
with make_tag('**********'):
    print('Челябинск')

# TEST_3:
with make_tag('--- Ломтик хлеба ---'):
    print('томат | салат | сыр | бекон')

# TEST_4:
with make_tag('*' * 20), make_tag(' ' * 5 + '-' * 10), make_tag(' ' * 7 + '=' * 6):
    print(' ' * 7 + 'привет')