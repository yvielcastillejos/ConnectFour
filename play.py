from score import*
from main import*

def playwithAI(move1, Board, depth):
        is_true = True
        moves = Get_Positions(Board)
        column1 = convert(move1)
        for row, column in moves:
            if column1 == column:
                row1 =row
        move1 = (row1,column1)
        Board =  drop_piece(Board, move1, 1)
        move2, _ =  miniMax(Board, depth, True)
        if move2 != None:
            Board  = drop_piece(Board, move2, 2)
        if state(Board) != -1: 
            Display(Board)
            if state(Board) == 1:
                print("Player 1 won")
            if state(Board) == 2:
                print("Player 2 won")
            if state(Board) == 0:
                print("Draw")
        return Board

def playinterminal():
    Board = BoardGame()
    is_true = True
    while is_true:
        Display(Board)
        print(f"Your turn! You have moves: {Get_Positions(Board)}")
        column1 = input("Enter a Column")
        row1 = input("Enter a Row")
        move1 = (int(column1), int(row1))
        Board =  drop_piece(Board, move1, 1)
        move2, _ =  miniMax(Board, 1, True)
        print(move2)
        if move2 != None:
            Board  = drop_piece(Board, move2, 2)
        if state(Board) != -1:
            Display(Board)
            if state(Board) == 1:
                print("Player 1 won")
            if state(Board) == 2:
                print("Player 2 won")
            if state(Board) == 0:
                print("Draw")
            is_true = False
    return


#print(convert(210))
                 
def convert(pos):
    if pos>=150 and pos<250:
       column = 0
    elif pos>=250 and pos<350:
       column = 1
    elif pos>=350 and pos<450:
       column = 2
    elif pos>=450 and pos<550:
       column = 3
    elif pos>=550 and pos<650:
       column = 4
    elif pos>=650 and pos<750:
       column = 5
    elif pos>=750 and pos<=850:
       column = 6
    else:
       column = 100
    return column

#print(convert(210))
#playinterminal()
