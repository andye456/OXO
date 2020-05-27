import numpy as np

# This get the human grid position to enter on the grid
class Human:

    def set_location(self,grid):
        a = np.where(grid == ' ')
        available = zip(a[0], a[1])
        print("Player turn, choose from the following locations:")
        print(available)
        select = raw_input(">")
        return eval(select)
