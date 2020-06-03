import random
import copy
import numpy as np


class Agent:

    def __init__(self):
        pass

    # This returns the location of the position on the grid to place the X or O
    def set_location(self,grid,method, model):
        # Find available positions
        # select a location to place the xoro
        if method == "random":
            select = _get_random_position(grid)
        if method == "neural":
            select = _get_neural_position(grid, model)
        return select

# Static private methods
# Returns the next position of the xoro randomly from the available positions
def _get_random_position(grid):
    # Find positions the contain a 0 (blank)
    available = _get_available_positions(grid)
    return random.choice(available)

# This is where the Neural network goes.
def _get_neural_position(grid, model):
    availableMoves = _get_available_positions(grid)
    maxValue = 0
    bestMove = availableMoves[0]
    for availableMove in availableMoves:
        # get a copy of a board
        boardCopy = copy.deepcopy(grid)
        value = model.predict(boardCopy, 0)
        if value > maxValue:
            maxValue = value
            bestMove = availableMove
    selectedMove = bestMove
    return selectedMove

def _get_available_positions(grid):
    a = np.where(grid == 0)
    return list(zip(a[0], a[1]))
