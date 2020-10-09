from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import InputLayer
import numpy as np
from organize_data import data, labels
from emotions import emodict

'''
File of the actual neural network model
'''

# Emotions
emotions = emodict()
emotions_list = [k for k, v in emotions.items()]

# Datasets
train_data, val_data = data()
train_labels, val_labels = labels()

seed = 7
np.random.seed(seed)

# Model
model = Sequential()
model.add(InputLayer(518))
model.add(Dense(512, activation='sigmoid'))
model.add(Dense(512, activation='sigmoid'))
model.add(Dense(len(emotions), activation='softmax'))

print(model.summary)

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
history = model.fit(train_data, train_labels, validation_data=(val_data, val_labels), epochs=100, batch_size=64, verbose=0)

# evaluate the model
loss, accuracy = model.evaluate(train_data, train_labels)
model.save(f'emotions_model_{accuracy*100:.2f}.h5')

print(f'Loss of the neural network: {loss} \nAccuracy of the neural network: {accuracy*100}%')

