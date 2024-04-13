from contextlib import contextmanager
@contextmanager
def safe_write(filename):
    try:
        file_old = open(filename, mode='r', encoding='utf-8')
        text_backup = file_old.readlines()
        file_old.close()
    except:
        pass
    file = open(filename, mode='w', encoding='utf-8')
    try:
        yield file
    except Exception as error:
        print(f'Во время записи в файл было возбуждено исключение {type(error).__name__}')
        file.close()
        file = open(filename, mode='w', encoding='utf-8')
        file.write(''.join(text_backup))
    finally:
        file.close()


with safe_write('under_tale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью\n')

with safe_write('under_tale.txt') as file:
    print('Под весёлый шорох листвы вы наполняетесь решительностью', file=file)
    raise ValueError

with open('under_tale.txt') as file:
    print(file.read())