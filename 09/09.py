    class TicTacToe:
        def __init__(self):
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.player = 'X'
            self.result = None
        def mark(self,x,y):
            _res = self.winner()
            if _res in ('Ничья','X','O'):
                print('Игра окончена')
                return
            x = x-1
            y = y-1
            if self.board[x][y] != ' ':
                print('Недоступная клетка')
                return
            else:
                self.board[x][y] = self.player
                if self.player == 'X':
                    self.player = 'O'
                else:
                    self.player = 'X'
        def winner(self):
            for i in range(3):
                if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i]!=' ':
                    return self.board[0][i]
                if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0]!=' ':
                    return self.board[i][0]
            if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0]!=' ':
                return self.board[i][0]

            if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[1][1] != ' ':
                return self.board[i][0]
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        return None
            return 'Ничья'

        def show(self):
            print(*self.board[0],sep='|')
            print('-----')
            print(*self.board[1], sep='|')
            print('-----')
            print(*self.board[2], sep='|')