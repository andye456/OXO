from RunGame import run_game
from model import TicTacToeModel


print("--- Summary ---")
history,x,o,d=run_game(player1="random", player2="random", loaded_model=None, iterations=10000)
print("X Wins = "+str(x))
print("O Wins = "+str(o))
print("Draws = "+str(d))
# Train the network using the results from the random games
ticTacToeModel = TicTacToeModel(9, 3, 100, 32)

model = ticTacToeModel.train(history)
model.save("OXO_model")
ticTacToeModel.set_model(model)
h, x, o, d = run_game(player1="neural", player2="random", loaded_model=ticTacToeModel, iterations=100)
print("After Learning (Neural = X vs Random = O):")
print("X Wins = "+str(x))
print("O Wins = "+str(o))
print("Draws = "+str(d))
# for i in range(10):
#     model = ticTacToeModel.train(h)
#     ticTacToeModel.set_model(model)
#     h, x, o, d = run_game(player1="neural", player2="random", loaded_model=ticTacToeModel, iterations=100)
#     print("After Learning (Neural = X vs Random = O):")
#     print("X Wins = "+str(x))
#     print("O Wins = "+str(o))
#     print("Draws = "+str(d))