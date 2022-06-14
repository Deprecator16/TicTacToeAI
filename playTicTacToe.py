from TicTacToeGame import TicTacToe
from TTTMinimaxAI import TTTMinimax
from TTTAlphaBetaAI import TTTAlphaBeta

import time

def getHumanInput(player):
    while True:
        row = int(input('Enter row number for player ' + player + ': ')) - 1
        col = int(input('Enter column number for player ' + player + ': ')) - 1
        if row < 0 or row > 2 or col < 0 or col > 2:
            print('Invalid row or column. Try again.')
        else:
            return row, col

def getAIInput(board, player):
    minimaxStart = time.perf_counter()
    m1, m2 = TTTMinimax(board, player)
    minimaxElapsed = time.perf_counter() - minimaxStart

    alphaBetaStart = time.perf_counter()
    ab1, ab2 = TTTAlphaBeta(board, player)
    alphaBetaElapsed = time.perf_counter() - alphaBetaStart

    print('Minimax: ', m1, ' ', m2, ' in ', minimaxElapsed, ' seconds')
    print('AlphaBeta: ', ab1, ' ', ab2, ' in ', alphaBetaElapsed, ' seconds')
    print ('Minimax to AlphaBeta ratio: ', minimaxElapsed / alphaBetaElapsed)
    return ab1, ab2

def getPlayerXInput(board, isHuman):
    if isHuman:
        return getHumanInput('X')
    else:
        return getAIInput(board, 'X')

def getPlayerOInput(board, isHuman):
    if isHuman:
        return getHumanInput('O')
    else:
        return getAIInput(board, 'O')

game = TicTacToe()
print(game)
while True:
    row, col = getPlayerXInput(game.board, True) if game.player == 'X' else getPlayerOInput(game.board, False)
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