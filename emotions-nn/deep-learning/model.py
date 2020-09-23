from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import InputLayer
import numpy as np
from organize_data import data, labels
from emotions import emodict
import matplotlib.pyplot as plt

'''
File of the actual neural network model
'''

# Emotions
emotions = emodict()

# Datasets
train_data, val_data, test_data = data()
train_labels, val_labels = labels()

seed = 7
np.random.seed(seed)

# Model
model = Sequential()
model.add(InputLayer(input_shape=(518, )))
model.add(Dense(512, activation='relu'))
model.add(Dense(512, activation='relu'))
model.add(Dense(len(emotions), activation='sigmoid'))

print(model.summary)

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
history = model.fit(train_data, train_labels, epochs=1000, batch_size=64, verbose=0)

# evaluate the model
loss, accuracy = model.evaluate(val_data, val_labels)

print(f'Loss of the neural network: {loss} \nAccuracy of the neural network: {accuracy*100}%')


