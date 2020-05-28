import random

from Agent import Agent
from Game import Game
import numpy as np
# Create a blank grid
from Human import Human

grid = np.empty((3, 3), dtype='str')
grid[:] = " "

# create the game
g = Game(grid)
agent1 = Agent()
agent2 = Agent()
human = Human()
X_wins = 0
O_wins = 0
Draws = 0
score = 0
it = 0
# Main game loop
while it < 1000:
    grid = g.get_grid()
    for i in ["X", "O"]:
        while True:
            if i == "X":
                loc = agent1.set_location(grid)
                # loc = human.set_location(grid)
                # Make sure the move is to a blank space before exiting the loop
                if g.make_move(loc,"X"):
                    break
            if i == "O":
                loc = agent2.set_location(grid)
                # Make sure the move is to a blank space before exiting the loop
                if g.make_move(loc,"O"):
                    break
        print(grid)
        res = g.check_win(grid)
        if res:
            print("Game: "+str(it))
            print(res)
            if res[:1] == 'X':
                X_wins+=1
                grid = np.empty((3, 3), dtype='str')
                grid[:] = " "
                g = Game(grid)
            elif res[:1] == 'O':
                O_wins+=1
                grid = np.empty((3, 3), dtype='str')
                grid[:] = " "
                g = Game(grid)
            else:
                Draws+=1
                grid = np.empty((3, 3), dtype='str')
                grid[:] = " "
                g = Game(grid)
            it += 1
            break
            # exit(1)
print("--- Summary ---")
print("X Wins = "+str(X_wins))
print("O Wins = "+str(O_wins))
print("Draws = "+str(Draws))