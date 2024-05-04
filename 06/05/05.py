class Reloopable:
    def __init__(self, file):
        self.file = file
    def __enter__(self):
        return [l.rstrip('\n') for l in self.file.readlines()]
    def __exit__(self, type, value, traceback):
        self.file.close()


# TEST_4:
files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt', 'file6.txt', 'file7.txt', 'file8.txt',
         'file9.txt', 'file10.txt', 'file11.txt', 'file12.txt', 'file13.txt', 'file14.txt', 'file15.txt', 'file16.txt',
         'file17.txt', 'file18.txt', 'file19.txt', 'file20.txt']

for file in files:
    with open(file, 'w') as f:
        pass

    f = open(file)
    print(f.closed)

    with Reloopable(f) as reloopable:
        pass

    print(f.closed)