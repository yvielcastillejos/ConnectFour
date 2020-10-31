import numpy as np
from weights import evaluationTable
import math
import random

def state(X):
    # Returns:
    #  -1 if playing
    #   0 if draw
    #   1 if player 1 wins
    #   2 if player 2 wins
    score = Win(X)
    moves = Get_Positions(X)
    if score == 10:
        return 1
    elif score == 20:
        return 2
    if len(moves) == 0:
        return 0
    return -1
 
def miniMax(board, depth, player):
    moves = Get_Positions(board)
    if depth == 0 or state(board) != -1:
        if state(board) ==2:
            return (None, 10000000)
        elif state(board) == 1:
            return (None, -10000000)
        elif state(board) == 0:
            return (None, 0)
        if depth == 0:
            return (None,int(eval(board)))
    if player:
        bestScore = -10000000
        bestMove = random.choice(moves)
        for move in moves:
            board_copy = board.copy()
            board_copy = drop_piece(board_copy, move, 2)
            newScore =  miniMax(board_copy, depth-1, False)[1]
            if newScore > bestScore:
                bestScore = newScore
                bestMove = move
        return bestMove, bestScore
    else:
        bestScore = 10000000
        bestMove = random.choice(moves)
        for move in moves:
            board_copy = board.copy()
            board_copy = drop_piece(board_copy, move, 1)
            newScore =  miniMax(board_copy, depth-1, True)[1]
            if  newScore < bestScore:
                bestScore = newScore
                bestMove = move
        return bestMove, bestScore

def drop_piece(board, move, player):
    if player == 1:
        board[move] = 1
    elif player == 2:
        board[move] = 2
    return board
    
def Get_Positions(X):
    # Gets positions that are available in the board and returns a list of those available
    accum = []
    column = 5
    row = 0
    is_true = True
    while is_true:
         if X[column][row] != 0:
             column-=1
             if column <0:
                 column = 5
                 row+=1
         if X[column][row] == 0:
             accum = accum + [(column,row)]
             column = 5
             row += 1
         if (len(accum) == 7) or (column == 0 and row ==6) or row >6 or column <0:
             is_true = False
    return accum

def Check(X):
    # Checks what moves will get a win for X and O and returns a two length array, 0 if none
    moves = Get_Positions(X)
    accumX = []
    accumY = []
    CopyBoard = X.copy() # Copies the board
    for i in moves:
            CopyBoard[i] 
            IsWin = Win(CopyBoard)
            if IsWin == 10:
                accumX = accumX + [i]
            elif IsWin == 20:
                accumY = accumY + [i]
            CopyBoard[i] = 0
    return [accumX,accumY]

def eval(board):
    utility = 138
    sum = 0
    for i in range(0,6,1):
        for j in range(0,7,1):
           if board[i][j] == 2:
               sum += evaluationTable[i][j]
           if board[i][j] == 1:
               sum -= evaluationTable[i][j]
    return sum + utility

def Win(Board):
    # general win condition returns a 10 if a win from X; 20 from O; and a 0 if neither
    # Horizontal
    X = Board.flatten()
    for j in range(0,6,1):
        for i in range(4*j+3*j,4*(j+1)+3*j,1):
          if (X[i]==X[i+1] == X[i+2]==X[i+3]==1):
              return 10
          if (X[i] == X[i + 1] == X[i + 2] == X[i + 3] == 2):
              return 20
    #Vertical
    for i in range(0,20,1):
        if (X[i]==X[i+7] == X[i+14]==X[i+21]==1):
            return 10
        if (X[i]==X[i+7] == X[i+14]==X[i+21]==2):
            return 20
    #RightDiagonal
    for j in range(0,3,1):
        for i in range(4*j+3*j,4*(j+1)+3*j,1):
            if (X[i]==X[i+8] == X[i+16]==X[i+24]==1):
                return 10
            if (X[i] == X[i + 8] == X[i + 16] == X[i + 24] == 2):
                return 20
    #LeftDiagonal
    for j in range(0,3,1):
        for i in range(4*j+3*j+3,4*(j+1)+3*j,1+3):
          if (X[i]==X[i+6] == X[i+12]==X[i+18]==1):
            return 10
          if (X[i] == X[i + 6] == X[i + 12] == X[i + 18] == 2):
            return 20
    return 0
