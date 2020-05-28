import random

import numpy as np


class Agent:

    def __init__(self):
        pass

    def set_location(self,grid,method="random"):
        # Find available positions
        # select a location to place the xoro
        if method == "random":
            select = self.get_random_position(grid)
        if method == "calc":
            select = self.calculate_position(grid)
        return select

    # Chooses the next position of the xoro randomly from the available positions
    # doesn't need to know where any of the other goes have gone.
    def get_random_position(self, grid):
        a = np.where(grid == ' ')
        available = list(zip(a[0], a[1]))
        return random.choice(available)

    def calculate_position(self, grid):
        pass