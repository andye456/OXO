import copy
from Agent import Agent
from Game import Game
import numpy as np
from Human import Human
from model import TicTacToeModel
import tensorflow as tf

history = []

# Main game loop
def run_game(player1, player2, loaded_model, iterations):
    grid = np.full((3, 3), 0)

    # create the game
    g = Game(grid)
    agent1 = Agent()
    agent2 = Agent()
    human = Human()

    score = 0
    moves = []
    output = 0
    # iterations = 1000
    it = 0
    X_wins = 0
    O_wins = 0
    Draws = 0
    while it < iterations:
        # The moves for each game
        for i in ["X", "O"]:
            while True:
                if i == "X":
                    loc = agent1.set_location(grid,player1,loaded_model)
                    # loc = human.set_location(grid)
                    # Make sure the move is to a blank space before exiting the loop
                    if g.make_move(loc,-1):
                        break
                if i == "O":
                    loc = agent2.set_location(grid,player2,loaded_model)
                    # loc = human.set_location(grid)
                    # Make sure the move is to a blank space before exiting the loop
                    if g.make_move(loc,1):
                        break
            # print(grid)
            res = g.check_win(grid)
            last_state = grid.tolist()
            moves.append(last_state)

            # Goes here if there is a result
            if res:
                print("Game: "+str(it))
                print(res)
                # X wins
                if res[:1] == 'X':
                    X_wins+=1
                    grid = np.full((3, 3), 0)
                    g = Game(grid)
                    output=-1
                # O wins
                elif res[:1] == 'O':
                    O_wins+=1
                    grid = np.full((3, 3), 0)
                    g = Game(grid)
                    output=1
                # Draw
                else:
                    Draws+=1
                    grid = np.full((3, 3), 0)
                    g = Game(grid)
                    output=0
                it += 1
                # If the game is won by less than nine moves then append the last board state to make the array 9 long.
                # Not sure how to make Keras deal with uneven data sizes
                while len(moves) < 9:
                    moves.append(last_state)
                for m in moves:
                    history.append((output,copy.deepcopy(m)))
                moves = []
                break
    return history,X_wins, O_wins, Draws

