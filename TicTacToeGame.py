class TicTacToe:
    def __init__(self):
        self.board = [[' '] * 3 for i in range(3)]
        self.player = 'X'

    def play(self, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2:
            print('Invalid row or column. Try again.')
            return False

        if self.board[row][col] == ' ':
            self.board[row][col] = self.player
            self.player = 'X' if self.player == 'O' else 'O'
            return True
        else:
            print('Invalid move. Try again.')
            return False

    def __str__(self):
        s = '   1 2 3\n'
        for i, row in enumerate(self.board):
            s += str(i + 1) + ' |'
            for col in row:
                s += col + '|'
            s += '\n'
        return s

    def isWinner(self, player):
        for row in self.board:
            if row.count(player) == 3:
                return True
        for i in range(3):
            if self.board[0][i] == player and self.board[1][i] == player and self.board[2][i] == player:
                return True
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        return False

    def isDraw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True
    