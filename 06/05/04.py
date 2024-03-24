class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename, 'r', encoding='utf-8')
        # _str = self.file.read().split('')
        # print(_str)
        return [l.rstrip('\n') for l in self.file.readlines()]

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

text = ''

with open('empty.txt', 'w', encoding='utf-8') as file:
    file.write(text)


with ReadableTextFile('empty.txt') as file:
    for line in file:
        print(line)