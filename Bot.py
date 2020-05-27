import random

import numpy as np


class Bot:

    def __init__(self):
        pass

    def set_location(self,grid):
        # Find available positions
        a = np.where(grid == ' ')
        available = zip(a[0], a[1])
        # select a random position
        select = random.choice(available)
        return select