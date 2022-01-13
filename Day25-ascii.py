import random

board = [[None]*3]*3


def pritnBoard():
    print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}\n----+----+----\n{board[1][0]}|{board[1][1]}|{board[1][2]}\n----+----+----\n{board[2][0]}|{board[2][1]}|{board[2][2]}")


def userTurn():
    user = 1
    while user:
        print("-"*10)
        pritnBoard()
        print()
        userChoiceX = input("What row do you what to play this turn?: ")
        userChoiceY = input("What coloumn do you what to play this turn?: ")
        try:
            userChoiceX, userChoiceY = int(userChoiceX)-1, int(userChoiceY)-1
            if board[userChoiceX][userChoiceY] == None:
                board[userChoiceX][userChoiceY] = "O"
                user = 1
            else:
                raise ValueError('ERROR')
        except:
            print("Input is not valid. Try again.")


def machineTurn():
    pass


pritnBoard()
userTurn()
pritnBoard()


def main():
    userTurn()
    print()
