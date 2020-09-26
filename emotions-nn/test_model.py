import tensorflow as tf
from organize_data import data, labels, test_data
from emotions import emodict
import pandas as pd
import numpy as np

model = tf.keras.models.load_model('model.h5')

# Emotions
emotions = emodict()
emotions_list = [k for k, v in emotions.items()]

test_data, titles, artists = test_data()

for i in range(36):
    prediction = model.predict(np.expand_dims(test_data[i], axis=0))

    emotion_index = np.argmax(prediction)

    emotion = emotions_list[emotion_index]

    print('----------------------------------------------------------')
    print(test_data[i])
    print(f'{titles[i]} is a {emotion.lower()} song. ')
