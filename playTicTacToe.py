from TicTacToeGame import TicTacToe
from TTTMinimaxAI import TTTMinimax
from TTTAlphaBetaAI import TTTAlphaBeta

def getHumanInput(player):
    while True:
        row = int(input('Enter row number for player ' + player + ': ')) - 1
        col = int(input('Enter column number for player ' + player + ': ')) - 1
        if row < 0 or row > 2 or col < 0 or col > 2:
            print('Invalid row or column. Try again.')
        else:
            return row, col

def getAIInput(board, player):
    useMinimax = False
    row, col = TTTMinimax(board, player) if useMinimax else TTTAlphaBeta(board, player)
    return row, col

def getPlayerXInput(board):
    isHuman = True
    if isHuman:
        return getHumanInput('X')
    else:
        return getAIInput(board, 'X')

def getPlayerOInput(board):
    isHuman = False
    if isHuman:
        return getHumanInput('O')
    else:
        return getAIInput(board, 'O')

game = TicTacToe()
print(game)
while True:
    row, col = getPlayerXInput(game.board) if game.player == 'X' else getPlayerOInput(game.board)
    game.play(row, col)
    print(game)
    if game.isWinner('X'):
        print('X wins')
        break
    elif game.isWinner('O'):
        print('O wins')
        break
    elif game.isDraw():
        print('Draw')
        break