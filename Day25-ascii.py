import random
import time

board = [["·" for i in range(3)]for j in range(3)]


def pritnBoard():
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} \n---+---+---\n {board[1][0]} | {board[1][1]} | {board[1][2]} \n---+---+---\n {board[2][0]} | {board[2][1]} | {board[2][2]} ")
    print("-"*10)


def userTurn():
    user = 1
    while user:
        userChoiceX = input("What row do you what to play this turn?: ")
        userChoiceY = input("What coloumn do you what to play this turn?: ")
        try:
            userChoiceX, userChoiceY = int(userChoiceX)-1, int(userChoiceY)-1
            if board[userChoiceX][userChoiceY] == "·" and userChoiceX >= 0 and userChoiceY >= 0:
                board[userChoiceX][userChoiceY] = "X"
                user = 0
            else:
                raise ValueError('ERROR')
        except:
            print("Input is not valid. Try again.")
    pritnBoard()

# Missing: Algorithem that chooses dinamiclly
def machineTurn():
    print("Machine is deciding...")
    time.sleep(random.randint(1, 3))
    print("-"*10)
    while True:
        x, y = random.randint(0, 2), random.randint(0, 2)
        if board[x][y] == "·":
            board[x][y] = "O"
            break
    pritnBoard()


def cheekWin():
    # Checks if the user won
    if any([1 for j in range(3) if sum([1 for i in range(3) if board[j][i] == "X"]) == 3]) or any([1 for j in range(3) if sum([1 for i in range(3) if board[i][j] == "X"]) == 3]) or all([1 if board[i][i] == "X" else 0 for i in range(3)]) or all([1 if board[i-1][3-i] == "X" else 0 for i in range(1, 4)]):
        print("You Win!")
        return 0
    # Checks if the PC has won
    elif any([1 for j in range(3) if sum([1 for i in range(3) if board[j][i] == "O"]) == 3]) or any([1 for j in range(3) if sum([1 for i in range(3) if board[i][j] == ""]) == 3]) or all([1 if board[i][i] == "O" else 0 for i in range(3)]) or all([1 if board[i-1][3-i] == "O" else 0 for i in range(1, 4)]):
        print("The computer wins!")
        return 0
    elif all([1 if board[i][j] != "·" else 0 for j in range(3) for i in range(3)]):
        print("Tie")
        return 0
    else:
        return 1


def main():
    playing = 1
    pritnBoard()
    while playing:
        userTurn()
        playing = cheekWin()
        if not playing:
            break
        machineTurn()
        playing = cheekWin()


if __name__ == "__main__":
    main()
