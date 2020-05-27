import numpy as np
import random

# Each move is evaluated as to how good it was given the current grid
# -1 if the move was a losing move
# +1 is the move was a winning move
# 0 is the move was neither
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
        if self.check_row_col(resX):
            return "X WIN"
        # Check if the O positions result in a win
        if self.check_row_col(resO):
            return "O WIN"
        # Check the diagonals
        if self.check_diagonals(zipX):
            return "X WIN"
        if self.check_diagonals(zipO):
            return "O WIN"

    # Checks that the positions give a win irrespective of whether it is Os or Xs
    def check_row_col(self,res):
        for g in res:
            if any(sublist in np.array_str(np.array(g[0])) for sublist in ('0 0 0', '1 1 1','2 2 2')):
                if '0 1 2' in np.array_str(np.array(g[1])):
                    return True

    def check_diagonals(self,res):
        # the diagonals
        if (0,0) in res and (1,1) in res and (2,2) in res:
            return True
        if (0,2) in res and (1,1) in res and (2,0) in res:
            return True

    # This gets
    def get_grid(self):
        return self.grid

    def make_move(self,x,y,XorO):
        if self.grid[x,y] == " ":
            self.grid[x,y] = XorO
            return True
        else:
            return False

"""

    def cpu_turn(self,grid):
        while True:
            xpos = random.randrange(0, 3)
            ypos = random.randrange(0, 3)
            print("trying: "+str(xpos)+","+str(ypos))
            if grid[xpos,ypos] == ' ':
                print("O goes: " + str(xpos) + "," + str(ypos))
                return str(xpos) + "," + str(ypos)
    

    
    # This is the basic game loop
    # Offers no control to a bot.x
    def play(self):
        grid = np.empty((3,3), dtype='str')
        grid[:] = " "
        print("Enter position: ")
        while True:
            for i in ["X","O"]:
                while True:
                    if i == "O":
                        pos=self.cpu_turn(grid)
                    else:
                        pos = raw_input(i + ">")
                    x=int(pos.split(",")[0])
                    y=int(pos.split(",")[1])
                    if grid[x,y] == " ":
                        grid[x,y] = i
                        print(grid)
                        res = self.check_win(grid)
                        if res:
                            print(res)
                            exit(1)
                        break
"""