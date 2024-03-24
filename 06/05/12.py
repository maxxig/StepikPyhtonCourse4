class TreeBuilder:
    def __init__(self):
        self._structure = {}
        self.lvl = 0
    def __enter__(self):
        self.lvl += 1
        self._structure[self.lvl] = []
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        t = self._structure[self.lvl]
        self._structure[self.lvl] = []
        self.lvl -= 1
        if t:
            if self.lvl in self._structure:
                self._structure[self.lvl].append(t)
            else:
                self._structure[self.lvl]= [t]


    def add(self, value):
        if self.lvl in self._structure:
            self._structure[self.lvl].append(value)
        else:
            self._structure[self.lvl] = [value]


    def structure(self):
        return self._structure[0] if len(self._structure)>0 else []

# TEST_7:
tree = TreeBuilder()

tree.add('1st')

with tree:
    with tree:
        with tree:
            with tree:
                tree.add('5th')

print(tree.structure())

# TEST_8:
tree1 = TreeBuilder()
tree2 = TreeBuilder()

tree1.add('1st')

with tree1:
    tree1.add('2nd')
    with tree1:
        tree1.add('3rd')
    tree1.add('4th')
    with tree1:
        pass

print(tree1.structure())
print(tree2.structure())

