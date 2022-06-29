from tkinter import *
from PIL import Image, ImageTk
import random
import time

# Note: Not finished

# Tkinter settings
root = Tk()
root.geometry('600x640')
root.title("TicTacToe")

imageX = ImageTk.PhotoImage(Image.open('images/x.png').resize((200, 200)))
imageO = ImageTk.PhotoImage(Image.open('images/o.png').resize((200, 200)))

# Logic code
userTurn = True
# Add the buttons to the board array
board = [[Button(root, padx=95, pady=95, command=lambda: userInput(i, j))
          for i in range(3)]for j in range(3)]
# Show the buttons with grid
[[board[i][j].grid(row=i, column=j) for i in range(3)]for j in range(3)]


def changeUI(x, y, symbol):
    button = board[x][y]
    if symbol == "x":
        button.config(image=imageX)
    elif symbol == "y":
        button.config(image=imageO)


def userInput(x, y):
    if userTurn:
        changeUI(x, y, "x")


def machineTurn():
    time.sleep(random.randint(1, 3))
    while True:
        x, y = random.randint(0, 2), random.randint(0, 2)
        if board[x][y] == "·":
            changeUI(x, y, "o")
            break


def cheekWin():
    # Checks if the user won
    if any([1 for j in range(3) if sum([1 for i in range(3) if board[j][i] == "X"]) == 3]) or any([1 for j in range(3) if sum([1 for i in range(3) if board[i][j] == "X"]) == 3]) or all([1 if board[i][i] == "X" else 0 for i in range(3)]) or all([1 if board[i-1][3-i] == "X" else 0 for i in range(1, 4)]):
        print("You Win!")
        return 0
    # Checks if the PC has won
    elif any([1 for j in range(3) if sum([1 for i in range(3) if board[j][i] == "O"]) == 3]) or any([1 for j in range(3) if sum([1 for i in range(3) if board[i][j] == ""]) == 3]) or all([1 if board[i][i] == "O" else 0 for i in range(3)]) or all([1 if board[i-1][3-i] == "O" else 0 for i in range(1, 4)]):
        print("The computer wins!")
        return 0
    # Checks for a tie
    elif all([1 if board[i][j] != "·" else 0 for j in range(3) for i in range(3)]):
        print("Tie")
        return 0
    # Else, we keep playing
    else:
        return 1


def main():
    print("board:", board)
    root.mainloop()

    """ playing = 1
    while playing:
        userTurn()
        playing = cheekWin()
        if not playing:
            break
        machineTurn()
        playing = cheekWin() """


if __name__ == "__main__":
    main()
