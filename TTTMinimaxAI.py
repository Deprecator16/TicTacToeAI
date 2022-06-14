def isWinner(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def isDraw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def minValue(board, player):
    if isWinner(board, player):
        return -1, None
    elif isWinner(board, 'X'):
        return 1, None
    elif isDraw(board):
        return 0, None
    v = 2
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                v2, _ = maxValue(board, 'X')
                board[i][j] = ' '
                if v2 < v:
                    v = v2
                    move = (i, j, player)
    return v, move

def maxValue(board, player):
    if isWinner(board, player):
        return 1, (-1, -1)
    elif isWinner(board, 'O'):
        return -1, (-1, -1)
    elif isDraw(board):
        return 0, (-1, -1)
    v = -2
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                v2, _ = minValue(board, 'O')
                board[i][j] = ' '
                if v2 > v:
                    v = v2
                    move = (i, j, player)
    return v, move

def TTTMinimax(board, player):
    if player == 'X':
        _, move = maxValue(board, player)
    else:
        _, move = minValue(board, player)
    return move[0], move[1]