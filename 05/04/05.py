class Matrix:
    def __init__(self, rows, cols, value = 0):
        self.rows = rows
        self.cols = cols
        self.maxrix = [[0 for i in range(cols)] for j in range(rows)]
    def get_value(self, rows, cols):
        return self.maxrix[rows][cols]
    def set_value(self, rows, cols, value):
        self.maxrix[rows][cols] = value
    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"
    def __str__(self):
        res = ''
        for j in range(self.rows):
            res += ' '.join([str(i) for i in self.maxrix[j]])
            res += '\n'
        return res.strip()

s = Matrix(2,3)
s.set_value(0,0,5)
print(s.get_value(0,0))
print(s.maxrix)
print(s)
