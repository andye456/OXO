import tensorflow as tf
from RunGame import run_game
from model import TicTacToeModel

ticTacToeModel = TicTacToeModel(9, 3, 100, 32)

# Get the model from the saved file
loaded_model = tf.keras.models.load_model("OXO_model")

# Set the model to use in the game to be the one just loaded
ticTacToeModel.set_model(loaded_model)
h, x, o, d = run_game(player1="neural", player2="random", loaded_model=ticTacToeModel, iterations=100)
print("After Learning (Neural = X vs Random = O):")
print("X Wins = " + str(x))
print("O Wins = " + str(o))
print("Draws = " + str(d))
# for i in range(5):
#     ticTacToeModel.train(h).save("OXO_model"+str(i))
#     loaded_model = tf.keras.models.load_model("OXO_model"+str(i))
#     ticTacToeModel.set_model(loaded_model)
#     h,x,o,d=run_game(player1="neural", player2="random", loaded_model=ticTacToeModel, iterations=100)
#     print("After Learning (Neural = X vs Random = O):")
#     print("X Wins = "+str(x))
#     print("O Wins = "+str(o))
#     print("Draws = "+str(d))

# # Create a second model from the data from playing using the first model.
# ticTacToeModel.train(h).save("OXO_model")
# loaded_model = tf.keras.models.load_model("OXO_model")
#
# _,x,o,d=run_game(player1="neural", player2="random", loaded_model=ticTacToeModel, iterations=100)
#
# print("After Learning (Neural = X vs Random = O):")
# print("X Wins = "+str(x))
# print("O Wins = "+str(o))
# print("Draws = "+str(d))