from contextlib import contextmanager
@contextmanager
def safe_open(filename, mode='r'):
    try:
        file = open(filename, mode)
        res_file, res_exept = file, None
    except Exception as e:
        res_file, res_exept = None, e
    finally:
        yield (res_file, res_exept)
    if res_file is not None:
        file.close()


# TEST_6:
with open('Couplet.txt', 'w') as file:
    file.write('Так уносились мы мечтой\n')
    file.write('К началу жизни молодой')

with safe_open('Couplet.txt') as file:
    file, error = file
    print(error)
    print(file.read())

    print(file.closed)

print(file.closed)