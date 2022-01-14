import random

board = [["·" for i in range(3)]for j in range(3)]


def pritnBoard():
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} \n---+---+---\n {board[1][0]} | {board[1][1]} | {board[1][2]} \n---+---+---\n {board[2][0]} | {board[2][1]} | {board[2][2]} ")


def userTurn():
    user = 1
    while user:
        print("-"*10)
        print()
        userChoiceX = input("What row do you what to play this turn?: ")
        userChoiceY = input("What coloumn do you what to play this turn?: ")
        try:
            userChoiceX, userChoiceY = int(userChoiceX), int(userChoiceY)
            if board[userChoiceX][userChoiceY] == "·":
                board[userChoiceX][userChoiceY] = "X"
                user = 0
            else:
                raise ValueError('ERROR')
        except:
            print("Input is not valid. Try again.")


def machineTurn():
    while True:
        x,y=random.randint(0,2),random.randint(0,2)
        if board[x][y]=="·":
            board[x][y]="O"
            break



def main():
    pritnBoard()
    userTurn()
    machineTurn()
    pritnBoard()


main()
