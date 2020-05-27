import random

from Bot import Bot
from Game import Game
import numpy as np
# Create a blank grid
from Human import Human

grid = np.empty((3, 3), dtype='str')
grid[:] = " "

# create the game
g = Game(grid)
bot = Bot()
human = Human()
# Main game loop
while True:
    grid = g.get_grid()
    for i in ["X", "O"]:
        while True:
            if i == "X":
                loc = bot.set_location(grid)
                # loc = human.set_location(grid)
                # Make sure the move is to a blank space before exiting the loop
                if g.make_move(loc,"X"):
                    break
            if i == "O":
                loc = bot.set_location(grid)
                # Make sure the move is to a blank space before exiting the loop
                if g.make_move(loc,"O"):
                    break
        print(grid)
        res = g.check_win(grid)
        if res:
            print(res)
            exit(1)
