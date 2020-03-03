import numpy as np

def Score(board):
    # takes in the board and determines the score for both black and white
    two_point = value(board, 2)
    three_point = value(board, 3)
    four_point = value(board, 4)
    points = two_point + three_point + four_point
    return points

def MiniMax(depth, X, maximizingPlayer):
    return 0

def Get_Positions(X):
    # Gets positions that are available in the board and returns a list of those available
    accum = []
    for i in range(35,42,1):
        if X[i] == 0:
            accum = accum + [i]
    for i in range(0,7,1):
        if X[i] != 0:
            accum = accum + [1000] # Means column is filled
    for i in range(0,35,1):
        if (X[i+7] != 0) and (X[i] == 0):
            accum = accum + [i]
    return accum

def getboundary(X):
    # gets the boundary positions of the board and returns an array
    boundary = Get_Positions(X)
    for i in range(0,len(boundary)):
        if boundary[i] != 1000:
            boundary[i] = boundary[i] + 7
    return boundary

def Check(X):
    # Checks what moves will get a win for X and O and returns a two length array, 0 if none
    moves = getboundary(X)
    accumX = []
    accumY = []
    CopyBoard = X.copy() # Copies the board
    for i in range(0,len(moves),1):
        if moves[i] != 1000:
            CopyBoard[i] = moves[i]
            IsWin = Win(CopyBoard)
            if IsWin == 10:
                accumX = accumX + [i]
            elif IsWin == 20:
                accumY = accumY + [i]
            CopyBoard[i] = 0
    if len(accumX) == 0:
        accumX = accumX + [0]
    if len(accumY) == 0:
        accumY = accumY + [0]
    return [accumX,accumY]

def value(board, streak):
    # calculates the points for each streak (2,3,or 4)
    # check Horizontal
    points = 0
    for j in range(0,6,1):
        for i in range(7*j,8-streak + 7*j,1):
           if board[i:i+streak] == [1]*streak:
              points += 1
           elif board[i:i+streak] == [2]*streak:
              points -= 1

    # for convenience for checking the vertical points
    boardf = []
    board_copy1 =  np.array([board[0:7],board[7:14],board[14:21],board[21:28],board[28:35]])
    board_transpose = board_copy1.transpose()
    board_copy2 = board_transpose.tolist()
    for i in range(0, len(board_copy2)):
        boardf = boardf + board_copy2[i]
    # check Vertical
    for j in range(0,7,1):
        for i in range(6*j,7-streak + 7*j,1):
          if boardf[i:i+streak] == [1]*streak:
              points += 1
          elif boardf[i:i+streak] == [2]*streak:
              points -= 1

    # For right diagonal
    if streak == 2:
        for j in range(0, 5, 1):
            for i in range(7*j, 7*j+6, 1):
                if board[i] == board[i + 8] == 1:
                    points += 1
                if board[i] == board[i + 8] == 2:
                    points -= 1
    if streak == 3:
        for j in range(0, 4, 1):
            for i in range(7*j, 7*j+5, 1):
                if board[i] == board[i + 8] == 1:
                    points += 1
                if board[i] == board[i + 8] == 2:
                    points -= 1
    if streak == 4:
        for j in range(0, 3, 1):
            for i in range(7*j, 7*j+4, 1):
                if board[i] == board[i + 8] == 1:
                    points += 1
                if board[i] == board[i + 8] == 2:
                    points -= 1

    # For left diagonal
    if streak == 2:
        for j in range(0, 5, 1):
            for i in range(7*j+1, 7*j+7, 1):
                if board[i] == board[i + 6] == 1:
                    points += 1
                if board[i] == board[i + 6] == 2:
                    points -= 1
    if streak == 3:
        for j in range(0, 4, 1):
            for i in range(7*j+2, 7*j+7, 1):
                if board[i] == board[i + 6] == 1:
                    points += 1
                if board[i] == board[i + 6] == 2:
                    points -= 1
    if streak == 4:
        for j in range(0, 3, 1):
            for i in range((7*j)+3, 7*j+7, 1):
                if board[i] == board[i + 6] == 1:
                    points +=1
                if board[i] == board[i + 6] == 2:
                    points -=1
    if streak == 2:
        points = points*10
    if streak == 3:
        points = points*100
    if streak == 4:
        points = points*1000
    return points

def Win(X):
    # eneral win condition returns a 10 if a win from X; 20 from O; and a 0 if neither
    # -----------------------#
    # Horizontal
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
