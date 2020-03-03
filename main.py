from Score import*

def Main(x):
    return 0

def BoardGame():
    A = [0]*6*7
    return A

def Display(B):
    #Displays the board in the terminal prompt
    accum = ""
    A = [0]*6*7
    for i in range(0,len(B),1):
        if B[i] == 0:
            A[i] = " "
        if B[i] == 1:
            A[i] = "X"
        if B[i] == 2:
            A[i] = "O"
    for i in range(1,6*7+1,1):
        accum = accum + str(A[i-1]) + str("    |  ")
        if (i%7) == 0:
            print(accum)
            print("------------------------------------------------------")
            accum = ''
    return

def ForConvenience():
    A = [0]*6*7
    for i in range(0,10,1):
        A[i] = str(0) + str(i)
    for i in range(10,6*7,1):
        A[i] = i
    return Displayhelper(A)

def Displayhelper(A):
    accum = ""
    for i in range(1,6*7+1,1):
        accum = accum + str(A[i-1]) + str("   |  ")
        if (i%7) == 0:
            print(accum)
            print("------------------------------------------------------")
            accum = ''
    return


def Generator(X):
    #takes in the board
    #Finds the next best possible move: AI by using minimax and calling score
    return

ForConvenience()

