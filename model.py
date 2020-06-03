from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical
import numpy as np


class TicTacToeModel:

    def __init__(self, numberOfInputs, numberOfOutputs, epochs, batchSize):
        self.epochs = epochs

        self.batchSize = batchSize
        self.numberOfInputs = numberOfInputs
        self.numberOfOutputs = numberOfOutputs
        self.model = Sequential()
        self.model.add(Dense(64, activation='relu', input_shape=(numberOfInputs, )))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(numberOfOutputs, activation='softmax'))
        self.model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    def train(self, dataset):
        input = []
        output = []
        for data in dataset:
            input.append(data[1])
            output.append(data[0])

        X = np.array(input).reshape((-1, self.numberOfInputs))
        # X = np.array(input).reshape((len(input), -1))
        y =to_categorical(output, num_classes=3)
        # Train and test data split this gives 80%
        boundary = int(0.8 * len(X))
        X_train = X[:boundary]
        X_test = X[boundary:]
        y_train = y[:boundary]
        y_test = y[boundary:]
        self.model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=self.epochs, batch_size=self.batchSize)
        # self.model.save('OXO_model')
        return self.model


    # This is to use a new model that has been loaded
    def set_model(self, model):
        self.model = model

    def predict(self, data, index):
        return self.model.predict(np.array(data).reshape(-1, self.numberOfInputs))[0][index]

