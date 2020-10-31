from score import*
import numpy as np

def BoardGame():
    A = np.zeros((6,7), dtype = int)
    return A

def Display(B):
    #Displays the board in the terminal prompt
    accum = ""
    A = np.zeros((6,7), dtype = int).tolist()
    for i in range(0,len(B),1):
        for j in range(0,len(B[0]),1):
           if B[i][j] == 0:
               A[i][j] = " "
           if B[i][j] == 1:
               A[i][j] = "X"
           if B[i][j] == 2:
               A[i][j] = "O"
    for i in range(0,len(B)):
        for j in range(0,len(B[0]),1):
            accum = accum + str(A[i][j]) + str("     |  ")
        print(accum)
        print("--------------------------------------------------------------")
        #print("---------------------------------------------------")
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
