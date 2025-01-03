import random
class Game:
    def __str__(self):
        print(*self.board, sep='\n')
        return ''
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = []
        #where i will create mines
        _mines = []
        s = 0
        for m in range(self.mines):
            while(1):
                _r = random.randint(0,self.rows-1)
                _c = random.randint(0, self.cols-1)
                if (_r,_c) not in _mines:
                    _mines.append((_r, _c))
                    s += 1
                    break
        # print(s)
        # s = 0
        for r in range(rows):
            _temp = []
            for c in range(cols):
                _cell = Cell(r,c)
                _temp.append(_cell)
            _t = _temp.copy()
            self.board.append(_t)
            _temp.clear()
        for _m in _mines:
            self.board[_m[0]][_m[1]].mine = True

        for r in range(rows):
            for c in range(cols):
                if self.board[r][c].mine == True:
                    for r_offset in range(-1, 2):
                        for c_offset in range(-1, 2):
                            if r_offset == 0 and c_offset == 0:
                                continue
                            if 0 <= r+r_offset < rows and 0 <= c+c_offset < cols:
                                self.board[r+r_offset][c+c_offset].neighbours +=1
        # print('s')



class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.mine = False
        self.neighbours = 0
    def __repr__(self):
        return f'{self.mine}|{self.neighbours}'
