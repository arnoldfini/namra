from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import InputLayer
from emotions import emodict
from input import extract_features
from ground_truth import get_ground_truth
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as split

emotions = emodict()
input_data = extract_features()
output_data = get_ground_truth()

input_data = np.asarray(input_data).astype(np.float32)
output_data = np.asarray(output_data).astype(np.float32)

'''
File of the actual neural network model
'''

seed = 7
np.random.seed(seed)

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


