from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import tensorflow as tf
import numpy as np
from tensorflow.keras.optimizers import SGD

# Build dataset
input_data = np.array([[40, 20], [60, 40], [80, 60]])
input_real = ["parka", "jacket", "raincoat"]

output_data = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])  # cloth

other = np.array([[30,20], [50,30]])

seed = 7
np.random.seed(seed)

model = Sequential()
model.add(Dense(8, input_dim=2, activation='sigmoid'))
model.add(Dense(256, input_dim=2, activation='sigmoid'))
model.add(Dense(3, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(input_data, output_data, epochs=1000, batch_size=32, verbose=0)

# evaluate the model
loss, accuracy = model.evaluate(input_data, output_data)


# calculate predictions
predictions = model.predict(other)

print(f"If temperature on range {other[0][0]}ºF & {other[0][1]}ºF : ")
print(f"Better take a {input_real[np.argmax(np.round(predictions))]}.")
