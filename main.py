import keyboard
import time
import sys

def createboard():
    board = []
    for i in range(3):
        board.append([" "] * 3)
    return board

def printboard(board):
    for i in range(3):
        print("|".join(board[i]))
        if i < 2:
            print("-----")

def checkwin(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def checkdraw(board):
    for row in board:
        if " " in row:
            return False
    return True

def playgame():
    board = createboard()
    current_player = "X"
    while True:
        printboard(board)
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))
            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter a number between 0 and 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 2.")
            continue

        if board[row][col] == " ":
            board[row][col] = current_player
            if checkwin(board):
                printboard(board)
                print(f"Player {current_player} wins!")
                break
            if checkdraw(board):
                printboard(board)
                print("It's a draw!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Cell already occupied. Try again.")

if __name__ == "__main__":
    playgame()

