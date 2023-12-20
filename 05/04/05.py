from copy import copy
class Matrix:
    def __init__(self, rows, cols, value = 0):
        self.rows = rows
        self.cols = cols
        self.maxrix = [[value for i in range(cols)] for j in range(rows)]
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
    def __pos__(self):
        res = Matrix(self.rows, self.cols)
        for j in range(self.rows):
            for i in range(self.cols):
                res.set_value(j, i, self.maxrix[j][i])
        return res
    def __neg__(self):
        res = Matrix(self.rows, self.cols)
        for j in range(self.rows):
            for i in range(self.cols):
                res.set_value(j, i, -self.maxrix[j][i])
        return res
    def __invert__(self):
        res = Matrix(self.cols, self.rows)
        for j in range(self.rows):
            for i in range(self.cols):
                res.set_value(i, j, self.maxrix[j][i])
        return res
    def __round__(self, n=None):
        res = Matrix(self.rows, self.cols)
        for j in range(self.rows):
            for i in range(self.cols):
                res.set_value(j, i, round(self.maxrix[j][i], n))
        return res


# TEST_8:
# TEST_9:
matrix = Matrix(2, 3, 1)

plus_matrix = +matrix
minus_matrix = -matrix
invert_matrix = ~matrix

print(plus_matrix.cols, plus_matrix.rows)
print(minus_matrix.cols, minus_matrix.rows)
print(invert_matrix.cols, invert_matrix.rows)