import tensorflow as tf
#from emotions_nn.organize_data import test_data
from emotions import emodict, emoreverse
import pandas as pd
import numpy as np


def predict_emotions(test_data):

    model = tf.keras.models.load_model(r'C:\Users\serio\PycharmProjects\namra\emotions_nn\model.h5')

    # Emotions
    emotions = emodict()
    emotions_list = [v for k, v in emotions.items()]

    # test_data, titles, artists = test_data()

    prediction = model.predict(np.expand_dims(test_data, axis=0))

    emotion_index = np.argmax(prediction)

    # Emotion to 2D
    emotion = emotions_list[emotion_index]

    # Returns the vector, e.g: [0.67 0.78]
    return emotion

