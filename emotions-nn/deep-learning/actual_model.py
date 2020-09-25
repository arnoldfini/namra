import tensorflow as tf
from organize_data import data, labels
from emotions import emodict
import numpy as np

# Emotions
emotions = emodict()
emotions_list = [k for k, v in emotions.items()]

train_data, val_data, test_data = data()

model = tf.keras.models.load_model('emotions_model_100.00')

prediction = model.predict_classes(test_data[0])
print(prediction)
exit()
emotion_index = prediction.index(np.argmax(prediction))
emotion = emotions_list[emotion_index]

print('----------------------------------------------------------')
print(f'This is a {emotion} song. ')
