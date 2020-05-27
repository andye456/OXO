import random

from Game import Game
import numpy as np
# Create a blank grid
grid = np.empty((3, 3), dtype='str')
grid[:] = " "

# create the game
g = Game(grid)

# Main game loop
while True:
    grid = g.get_grid()
    print(grid)
    # Find available positions
    a = np.where(grid == ' ')
    available = zip(a[0],a[1])
    print (available)
    print("--------")
    select = random.choice(available)
    print(select)