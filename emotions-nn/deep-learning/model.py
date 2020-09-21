from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import InputLayer
import numpy as np
from organize_data import data
import matplotlib.pyplot as plt

'''
File of the actual neural network model
'''

# Datasets
train_data, val_data, test_data, output_data = data()

seed = 7
np.random.seed(seed)

# Model
model = Sequential()
model.add(InputLayer(input_shape=(518, )))
model.add(Dense(512, activation='relu'))
model.add(Dense(512, activation='relu'))
model.add(Dense(len(output_data), activation='sigmoid'))

print(model.summary)

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

# Fit the model
history = model.fit(input_data, output_data, epochs=10, batch_size=64, verbose=0)

# evaluate the model
loss, accuracy = model.evaluate(input_data, output_data)

print(f'Loss of the neural network: {loss} \nAccuracy of the neural network: {accuracy*100}%')


