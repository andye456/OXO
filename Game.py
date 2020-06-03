import numpy as np
import random

# Each move is evaluated as to how good it was given the current grid
class Game:

    def __init__(self,grid):
        self.training_history = []
        self.grid = grid
        self.bin_state = 0b00000000000000000000000000

    def check_win(self, grid):
        # Finds the positions of the Xs or Os in the grid
        resX = [np.where(grid == -1), np.where(np.transpose(grid) == -1)]
        resO = [np.where(grid == 1), np.where(np.transpose(grid) == 1)]

        # Gets the coordinates of the places occupied by X or O
        zipX=list(zip(np.where(grid == -1)[0],np.where(grid == -1)[1]))
        zipO=list(zip(np.where(grid == 1)[0],np.where(grid == 1)[1]))

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
        # Check if the board is full
        elif np.where(grid == 0)[0].size == 0:
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

    # This gets the current grid
    def get_grid(self):
        return self.grid

    # returns a binary representation of the game state
    def get_game_state(self):
        x=0b000000000
        o=0b000000000
        b=0b000000000
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                if self.grid[i][j] == "X":
                    mask = 0b000000001 << 3*i+j
                    old_x = x
                    x = old_x | mask
                elif self.grid[i][j] == "O":
                    mask = 0b000000001 << 3*i+j
                    old_o = o
                    o = old_o | mask
                else:
                    mask = 0b000000001 << 3*i+j
                    old_b = b
                    b = old_b | mask
        str_res = format(x, '09b')+format(o, '09b')+format(b,'09b')
        bin_state =  ''.join(i for i in str_res)
        return int(bin_state,2)

    def make_move(self,pos,XorO):
        if self.grid[pos] == 0:
            self.grid[pos] = XorO
            return True
        else:
            return False

