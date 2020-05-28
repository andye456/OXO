import numpy as np
import random

# Each move is evaluated as to how good it was given the current grid
class Game:

    def __init__(self,grid):
        self.grid = grid

    def check_win(self, grid):
        # Finds the positions of the Xs or Os in the grid
        resX = [np.where(grid == 'X'), np.where(np.transpose(grid) == 'X')]
        resO = [np.where(grid == 'O'), np.where(np.transpose(grid) == 'O')]

        # Gets the coordinates of the places occupied by X or O
        zipX=zip(np.where(grid == 'X')[0],np.where(grid == 'X')[1])
        zipO=zip(np.where(grid == 'O')[0],np.where(grid == 'O')[1])

        # Check if the X positions result in a win
        if self._check_row_col(resX):
            return "X WIN"
        # Check if the O positions result in a win
        elif self._check_row_col(resO):
            return "O WIN"
        # Check the diagonals
        elif self._check_diagonals(zipX):
            return "X WIN"
        elif self._check_diagonals(zipO):
            return "O WIN"
        elif np.where(grid == ' ')[0].size == 0:
            # If there are no lines of 3 for XorO and the grid contains no more empty spaces
            return "DRAW"


    # Checks that the positions give a win irrespective of whether it is Os or Xs
    def _check_row_col(self, res):
        for g in res:
            if any(sublist in np.array_str(np.array(g[0])) for sublist in ('0 0 0', '1 1 1','2 2 2')):
                if '0 1 2' in np.array_str(np.array(g[1])):
                    return True

    def _check_diagonals(self, res):
        # the diagonals
        if (0,0) in res and (1,1) in res and (2,2) in res:
            return True
        if (0,2) in res and (1,1) in res and (2,0) in res:
            return True

    # This gets
    def get_grid(self):
        return self.grid

    def make_move(self,pos,XorO):
        if self.grid[pos] == " ":
            self.grid[pos] = XorO
            return True
        else:
            return False
