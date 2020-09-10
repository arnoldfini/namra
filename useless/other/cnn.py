import tensorflow as tf
import tensorflow.keras
import numpy as np
import os
import librosa
import matplotlib.pyplot as plt

audio_path = r'C:\Users\serio\OneDrive\Escritorio\clips_full\1'
x , sr = librosa.load(audio_path)
print(type(x), type(sr))

'''
input = np.array([])

for i in range(1, 1000):
    with open(f'clips_full\{i}') as f:
        input[i] = tf.f.stft(
            f, frame_length, frame_step, fft_length=None,
            window_fn=tf.signal.hann_window, pad_end=False, name=None
        )

'''


'''
for i in range(len(input)):

    input[i]= tf.i.stft(
        signals, frame_length, frame_step, fft_length=None,
        window_fn=tf.signal.hann_window, pad_end=False, name=None
    )




model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv3D(32, (64,128,16), activation='relu'))
model.add(tf.keras.layers.MaxPooling3D((64,128,16)))
model.add(tf.keras.layers.Conv3D(64, (32,64,32), activation='relu'))
model.add(tf.keras.layers.MaxPooling3D((64,32,64)))
model.add(tf.keras.layers.Conv3D(64, (16,32,64), activation='relu'))
model.add(tf.keras.layers.MaxPooling3D((16,32,64)))
model.add(tf.keras.layers.Dense(1024, activation='relu'))
model.add(tf.keras.layers.Dense(4))
'''
'''

tf.keras.optimizers.SGD(
    learning_rate=0.01, momentum=0.0, nesterov=False, name='SGD', **kwargs
)

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=85,
                    validation_data=(test_images, test_labels))
'''
