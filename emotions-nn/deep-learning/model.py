import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

'''
File of the actual neural network model
'''

model = Sequential()
model.add(Dense(64, input_dim=2, activation=relu))
model.add(Dense(64, input_dim=2, activation=relu))