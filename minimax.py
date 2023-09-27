import numpy as np

currentBoardState = ["O", "X", "X", "X", "X", "O", 6, "O", 8]
emptyBoard = [0,1,2,3,4,5,6,7,8]

def getLegalMoves(currBrdState):
    legalMoves = []
    for i in currBrdState:
        if i != "X" and i != "O":
            legalMoves.append(i)

    return legalMoves

def checkWinner(currBrdState):
    if (
    (currBrdState[0] == "X" and currBrdState[1] == "X" and currBrdState[2] == "X") or
    (currBrdState[3] == "X" and currBrdState[4] == "X" and currBrdState[5] == "X") or
    (currBrdState[6] == "X" and currBrdState[7] == "X" and currBrdState[8] == "X") or
    (currBrdState[0] == "X" and currBrdState[3] == "X" and currBrdState[6] == "X") or
    (currBrdState[1] == "X" and currBrdState[4] == "X" and currBrdState[7] == "X") or
    (currBrdState[2] == "X" and currBrdState[5] == "X" and currBrdState[8] == "X") or
    (currBrdState[0] == "X" and currBrdState[4] == "X" and currBrdState[8] == "X") or
    (currBrdState[2] == "X" and currBrdState[4] == "X" and currBrdState[6] == "X")
):
        return 3
    elif (
    (currBrdState[0] == "O" and currBrdState[1] == "O" and currBrdState[2] == "O") or
    (currBrdState[3] == "O" and currBrdState[4] == "O" and currBrdState[5] == "O") or
    (currBrdState[6] == "O" and currBrdState[7] == "O" and currBrdState[8] == "O") or
    (currBrdState[0] == "O" and currBrdState[3] == "O" and currBrdState[6] == "O") or
    (currBrdState[1] == "O" and currBrdState[4] == "O" and currBrdState[7] == "O") or
    (currBrdState[2] == "O" and currBrdState[5] == "O" and currBrdState[8] == "O") or
    (currBrdState[0] == "O" and currBrdState[4] == "O" and currBrdState[8] == "O") or
    (currBrdState[2] == "O" and currBrdState[4] == "O" and currBrdState[6] == "O")
    ):
        return 1
        

    elif len(getLegalMoves(currBrdState)) == 0:
        return int(2)

    else:
        return False

def printWinner(currBrdState):
    if (
    (currBrdState[0] == "X" and currBrdState[1] == "X" and currBrdState[2] == "X") or
    (currBrdState[3] == "X" and currBrdState[4] == "X" and currBrdState[5] == "X") or
    (currBrdState[6] == "X" and currBrdState[7] == "X" and currBrdState[8] == "X") or
    (currBrdState[0] == "X" and currBrdState[3] == "X" and currBrdState[6] == "X") or
    (currBrdState[1] == "X" and currBrdState[4] == "X" and currBrdState[7] == "X") or
    (currBrdState[2] == "X" and currBrdState[5] == "X" and currBrdState[8] == "X") or
    (currBrdState[0] == "X" and currBrdState[4] == "X" and currBrdState[8] == "X") or
    (currBrdState[2] == "X" and currBrdState[4] == "X" and currBrdState[6] == "X")
):
        print("X Wins!")
    elif (
    (currBrdState[0] == "O" and currBrdState[1] == "O" and currBrdState[2] == "O") or
    (currBrdState[3] == "O" and currBrdState[4] == "O" and currBrdState[5] == "O") or
    (currBrdState[6] == "O" and currBrdState[7] == "O" and currBrdState[8] == "O") or
    (currBrdState[0] == "O" and currBrdState[3] == "O" and currBrdState[6] == "O") or
    (currBrdState[1] == "O" and currBrdState[4] == "O" and currBrdState[7] == "O") or
    (currBrdState[2] == "O" and currBrdState[5] == "O" and currBrdState[8] == "O") or
    (currBrdState[0] == "O" and currBrdState[4] == "O" and currBrdState[8] == "O") or
    (currBrdState[2] == "O" and currBrdState[4] == "O" and currBrdState[6] == "O")
    ):
        print("O Wins!")
        
    elif len(getLegalMoves(currBrdState)) == 0:
        print("It's a Tie!")
    else:
        return False


def getCurrMark(currBrdState):
    X_Counter = 0
    O_Counter = 0
    for i in currBrdState:
        if i == "X":
            X_Counter += 1
        elif i == "O":
            O_Counter += 1
    
    if X_Counter == O_Counter:
        return "X"
    elif X_Counter > O_Counter:
        return "O"
    
def getNextState(currBrdState, action):
    nextBrdState = currBrdState.copy()
    if getCurrMark(nextBrdState) == "X":
        nextBrdState[action] = "X"
        return nextBrdState
    elif getCurrMark(nextBrdState) == "O":
        nextBrdState[action] = "O"
        return nextBrdState
    

def maxValue(currBrdState):
    if checkWinner(currBrdState) == False:
        bestValue = -9999
        bestAction = None

        for action in getLegalMoves(currBrdState):
            value, _ =  minValue(getNextState(currBrdState, action))
            if value > bestValue:
                bestValue = value
                bestAction = action
            
        return bestValue, bestAction

    else:
        score = checkWinner(currBrdState)
        return score, None


def minValue(currBrdState):
    if checkWinner(currBrdState) == False:
        bestValue = 9999
        bestAction = None

        for action in getLegalMoves(currBrdState):
            value, _ = maxValue(getNextState(currBrdState, action))
            if value < bestValue:
                bestValue = value
                bestAction = action
        return bestValue, bestAction
    
    else: 
        score = checkWinner(currBrdState)
        return score, None

    





def playGameManually(currBrdState):
    if checkWinner(currBrdState) == False:
        if getCurrMark(currBrdState) == "X":
            utility, position = maxValue(currBrdState)
            return position
        elif getCurrMark(currBrdState) == "O":
            utility, position = minValue(currBrdState)
            return position
    elif checkWinner(currBrdState) == 3:
        return "X Wins!"
    elif checkWinner(currBrdState) == 2:
        return "It's a Tie!"
    elif checkWinner(currBrdState) == 1:
        return "O Wins!"
    

def playGame():
    board = [0,1,2,3,4,5,6,7,8]
    playerAssignment = input("Which player do you wanna be? X or O? ")
    if playerAssignment == "X":
        boardPrinter(board)
        move = int(input("You start! Type the position you wanna play! (from 0 to 8) "))
        board[move] = "X"
        boardPrinter(board)

        while checkWinner(board) == False:
            if getCurrMark(board) == "O":
                print("It's AI's turn!")
                utility, position = minValue(board)
                board[position] = "O"
                boardPrinter(board)
                messageWriter(board)
            
            elif getCurrMark(board) == "X":
                print("It's your turn!")
                move = int(input("Where do you wanna play next? (from 0 to 8) "))
                board[move] = "X"
                boardPrinter(board)
        messageWriter(board)        

                

    elif playerAssignment == "O":
        utility, position = maxValue(board)
        board[position] = "X"
        boardPrinter(board)

        while checkWinner == False:
            if getCurrMark(board) == "O":
                print("It's your turn!")
                move = int(input("Where do you wanna play next? (from 0 to 8) "))
                board[move] = "X"
                boardPrinter(board)


            elif getCurrMark(board) == "X":
                print("It's AI's turn!")
                utility, position = maxValue(board)
                board[position] = "X"
                boardPrinter(board)
        messageWriter(board)        


def boardPrinter(currBrdState):
    readableBoard = np.array([[currBrdState[0], currBrdState[1], currBrdState[2]],
                              [currBrdState[3], currBrdState[4], currBrdState[5]],
                              [currBrdState[6], currBrdState[7], currBrdState[8]]])


    print(readableBoard)


def messageWriter(currBrdState):
    if checkWinner(currBrdState) == False:
        return
    elif checkWinner(currBrdState) == 3:
        print("X Wins!")
    elif checkWinner(currBrdState) == 2:
        print("It's a Tie!")
    elif checkWinner(currBrdState) == 1:
        print("O Wins!")








    




