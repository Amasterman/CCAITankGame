import numpy as np
from tkinter import *


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
        elif self.direction == ">":
            self.direction = "^"
        elif self.direction == "<":
            self.direction = "v"
        elif self.direction == "v":
            self.direction = ">"

    def turn_right(self):
        if self.direction == "^":
            self.direction = ">"
        elif self.direction == ">":
            self.direction = "v"
        elif self.direction == "<":
            self.direction = "^"
        elif self.direction == "v":
            self.direction = "<"

    def move(self):
        if self.direction == "^":
            self.y -= 1
        elif self.direction == ">":
            self.x += 1
        elif self.direction == "<":
            self.x -= 1
        elif self.direction == "v":
            self.y += 1

    def shoot(self):
        pass


class GameGUI:
    def __init__(self, root, player, board_size):
        self.root = root
        self.player = player
        self.board_size = board_size
        self.output_label = Label(root, text="")
        self.output_label.grid(row=board_size[0]+4, column=0, columnspan=board_size[1])

        # Create a label and textbox for player passcode
        Label(root, text="Enter your passcode: ").grid(row=0, column=0)
        self.passcode_entry = Entry(root)
        self.passcode_entry.grid(row=0, column=1)
        self.passcode_submit = Button(root, text="Submit", command=self.identify)
        self.passcode_submit.grid(row=0, column=2)

        self.canvas = Canvas(root, width=board_size[1]*50, height=board_size[0]*50)
        self.canvas.grid(row=1, column=0, columnspan=board_size[1])

        # Create rectangles for each element of the board
        for i in range(board_size[0]):
            for j in range(board_size[1]):
                self.canvas.create_rectangle(j*50, i*50, (j+1)*50, (i+1)*50)

        # Create arrow for the player
        self.player_arrow = self.canvas.create_polygon(player.x*50+25, player.y*50+25, player.x*50+35, player.y*50+15, player.x*50+15, player.y*50+15, fill="red")
        self.rotate_player_arrow()

        # Create buttons for each move option
        self.turn_left_button = Button(root, text="Turn Left", command=self.turn_left)
        self.turn_left_button.grid(row=board_size[0]+1, column=0)
        self.turn_right_button = Button(root, text="Turn Right", command=self.turn_right)
        self.turn_right_button.grid(row=board_size[0]+1, column=1)
        self.move_button = Button(root, text="Move", command=self.move)
        self.move_button.grid(row=board_size[0]+1, column=2)
        self.shoot_button = Button(root, text="Shoot", command=self.shoot)
        self.shoot_button.grid(row=board_size[0]+1, column=3)

        def rotate_player_arrow(self):
            if self.player.direction == "^":
                self.canvas.itemconfig(self.player_arrow, points=[self.player.x * 50 + 25, self.player.y * 50 + 25,
                                                                  self.player.x * 50 + 35, self.player.y * 50 + 15,
                                                                  self.player.x * 50 + 15, self.player.y * 50 + 15])
            elif self.player.direction == ">":
                self.canvas.itemconfig(self.player_arrow, points=[self.player.x * 50 + 35, self.player.y * 50 + 25,
                                                                  self.player.x * 50 + 45, self.player.y * 50 + 35,
                                                                  self.player.x * 50 + 35, self.player.y * 50 + 15])
            elif self.player.direction == "v":
                self.canvas.itemconfig(self.player_arrow, points=[self.player.x * 50 + 25, self.player.y * 50 + 35,
                                                                  self.player.x * 50 + 35, self.player.y * 50 + 45,
                                                                  self.player.x * 50 + 15, self.player.y * 50 + 35])
            elif self.player.direction == "<":
                self.canvas.itemconfig(self.player_arrow, points=[self.player.x * 50 + 15, self.player.y * 50 + 25,
                                                                  self.player.x * 50 + 25, self.player.y * 50 + 35,
                                                                  self.player.x * 50 + 25, self.player.y * 50 + 15])

        def turn_left(self):
            self.disable_move_buttons()
            self.turn_left_button.config(state=DISABLED, relief=SUNKEN)
            self.player.turn_left()
            self.rotate_player_arrow()

        def turn_right(self):
            self.disable_move_buttons()
            self.turn_right_button.config(state=DISABLED, relief=SUNKEN)
            self.player.turn_right()
            self.rotate_player_arrow()

        def move(self):
            self.disable_move_buttons()
            self.move_button.config(state=DISABLED, relief=SUNKEN)
            self.player.move()
            self.canvas.move(self.player_arrow, (self.player.x - self.player.prev_x) * 50,
                             (self.player.y - self.player.prev_y) * 50)

        def shoot(self):
            self.disable_move_buttons()
            self.shoot_button.config(state=DISABLED, relief=SUNKEN)
            self.player.shoot()

        def submit(self):
            if self.turn_left_button["state"] == DISABLED:
                    self.player.turn_left()
                    self.rotate_player_arrow()
                    self.output_label.config(text="Player turned left.")
            elif self.turn_right_button["state"] == DISABLED:
                    self.player.turn_right()
                    self.rotate_player_arrow()
                    self.output_label.config(text="Player turned right.")
            elif self.move_button["state"] == DISABLED:
                    self.player.move()
                    self.canvas.move(self.player_arrow, (self.player.x - self.player.prev_x) * 50, (self.player.y - self.player.prev_y) * 50)
                    self.output_label.config(text="Player moved.")
            elif self.shoot_button["state"] == DISABLED:
                    self.player.shoot()
                    self.output_label.config(text="Player shot.")
            self.enable_move_buttons()

if __name__ == "__main__":
    board_size = (5,5)
    board = np.array([["." for _ in range(board_size[1])] for _ in range(board_size[0])])
    root = Tk()
    player1 = Player(1, "abc", 0, 0, "^")
    game = GameGUI(root, player1, board_size)
    root.mainloop()