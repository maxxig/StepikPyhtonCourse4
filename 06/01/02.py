class DevelopmentTeam:
    def __init__(self):
        self.junior = []
        self.seniors = []
    def add_junior(self, *args):
        self.junior.extend(args)
        # print('s')
    def add_senior(self, *args):
        self.seniors.extend(args)
    def __iter__(self):
        yield from iter([(j, 'junior') for j in self.junior])
        yield from iter([(s, 'senior') for s in self.seniors])


beegeek = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
print(*beegeek, sep='\n')
