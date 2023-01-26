import numpy as np
from tkinter import *

# Initialize the game board size
board_size = (10, 10)

# Initialize the game board as a grid filled with dots
board = np.full(board_size, " ")


# Class to represent a player
class Player:
    def __init__(self, number, passcode, x, y, direction):
        self.number = number
        self.passcode = passcode
        self.x = x
        self.y = y
        self.direction = direction

    def identify(self, passcode_entry):
        input_passcode = passcode_entry.get()
        if input_passcode != self.passcode:
            return False
        return True

    def turn_left(self):
        if self.direction == "^":
            self.direction = "<"
        elif self.direction == "<":
            self.direction = "v"
        elif self.direction == "v":
            self.direction = ">"
        elif self.direction == ">":
            self.direction = "^"

    def turn_right(self):
        if self.direction == "^":
            self.direction = ">"
        elif self.direction == ">":
            self.direction = "v"
        elif self.direction == "v":
            self.direction = "<"
        elif self.direction == "<":
            self.direction = "^"

    def move(self):
        if self.direction == "^":
            self.y -= 1
        elif self.direction == ">":
            self.x += 1
        elif self.direction == "v":
            self.y += 1
        elif self.direction == "<":
            self.x -= 1
        # check if the new position is within the grid
        if self.x < 0 or self.x >= board_size[0] or self.y < 0 or self.y >= board_size[1]:
            print("Invalid move. Player is out of the grid.")
            self.x = max(0, min(self.x, board_size[0] - 1))
            self.y = max(0, min(self.y, board_size[1] - 1))

    def shoot(self):
        if self.direction == "^":
            x, y = self.x, self.y - 1
        elif self.direction == ">":
            x, y = self.x + 1, self.y
        elif self.direction == "v":
            x, y = self.x, self.y + 1
        elif self.direction == "<":
            x, y = self.x - 1, self.y
        # check if the shooting position is within the grid
        if x < 0 or x >= board_size[0] or y < 0 or y >= board_size[1]:
            print("Invalid shoot. Player is out of the grid.")
            return
        # code to check if there's a target on the shooting position
        if board[x][y] != ".":
            print("Player", self.number, "hit target!")
        else:
            print("Player", self.number, "missed.")

class Game:
    def __init__(self, board, board_size, board_labels):
        self.board = board
        self.board_size = board_size
        self.board_labels = board_labels

    def update_board(self):
        for i in range(self.board_size[0]):
            for j in range(self.board_size[1]):
                self.board_labels[i][j].config(text=self.board[i][j])


class GameGUI:
    def __init__(self, root, player, board, board_size):
        self.root = root
        self.player = player
        self.board = board
        self.board_size = board_size
        self.output_label = Label(root, text="")
        self.output_label.grid(row=board_size[0] + 2, column=0, columnspan=board_size[1])

        # Create a label and textbox for player passcode
        Label(root, text="Enter your passcode: ").grid(row=0, column=0)
        self.passcode_entry = Entry(root)
        self.passcode_entry.grid(row=0, column=1)

        # Create labels for each element of the board
        self.board_labels = [[Label(root, text="", width=2, height=1) for j in range(board_size[1])] for i in
                             range(board_size[0])]
        for i in range(board_size[0]):
            for j in range(board_size[1]):
                self.board_labels[i][j].grid(row=i + 1, column=j)

        # Create buttons for each move option
        self.turn_left_button = Button(root, text="Turn Left", command=self.turn_left)
        self.turn_left_button.grid(row=board_size[0] + 1, column=0)
        self.turn_right_button = Button(root, text="Turn Right", command=self.turn_right)
        self.turn_right_button.grid(row=board_size[0] + 1, column=1)
        self.move_button = Button(root, text="Move", command=self.move)
        self.move_button.grid(row=board_size[0] + 1, column=2)
        self.shoot_button = Button(root, text="Shoot", command=self.shoot)
        self.shoot_button.grid(row=board_size[0] + 1, column=3)

        self.update_board()

def add_player(board, player_number, x, y, direction):
    if x < 0 or x >= board_size[0] or y < 0 or y >= board_size[1]:
        print("Invalid coordinates. Please enter coordinates between 0 and {}.".format(board_size[0]-1,board_size[1]-1))
        return
    player = Player(player_number, x, y, direction)
    board[x][y] = direction
    for i in range(board_size[0]):
        for j in range(board_size[1]):
            board_labels[i][j].config(text=board[i][j])
    return player


# Print Board
def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
            print()

root = Tk()
root.title("Game")

#Initialize the game board and player
board_size = (10,10)
board = np.full(board_size, " ")
player1 = Player(1, "passcode1", 5, 5, "^")

#Initialize the board_labels
board_labels = [[Label(root, text=board[i][j]) for j in range(board_size[1])] for i in range(board_size[0])]
for i in range(board_size[0]):
    for j in range(board_size[1]):
        board_labels[i][j].grid(row=i, column=j)



root.mainloop()