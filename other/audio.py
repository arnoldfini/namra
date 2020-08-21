import matplotlib.pyplot as plt
import librosa
import librosa.display
import os
import glob
from eyed3 import id3
from time import sleep
import numpy as np
import sklearn

'''
Test
'''

dir = r'C:\Users\serio\OneDrive\Escritorio\test'

i = 0
for j in range(len(dir)):
    i += 1

print(i)

'''
---------------
'''




prefix_path= (r'C:\Users\serio\OneDrive\Escritorio\test')
file_array = [f for f in os.listdir(prefix_path) if f.endswith('.mp3')]
file_array.sort()

file_array = [os.path.join(prefix_path, name) for name in file_array]

print('Starting...')

fourier = np.empty([1025])

for i in range(len(file_array)):

    tag = id3.Tag()
    tag.parse(file_array[i])

    x, sr = librosa.load(file_array[i], sr=44100)

    plt.figure(figsize=(14,5))
    librosa.display.waveplot(x, sr=sr)
    plt.title(tag.title)

#    plt.show()

    print(i)

np.vstack([fourier, librosa.stft(x)])

np.savetxt('fourier.csv', fourier, delimiter=',')



exit(0)

# Create graph and save it as .png

for i in range(len(file_array)):

    X = librosa.stft(x)
    Xdb = librosa.amplitude_to_db(abs(X))
    plt.figure(figsize=(14,5))
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
    plt.colorbar()


    try:
        title = str(tag.title).replace('"', '"')

        plt.savefig(rf'C:\Users\serio\classical music\random\{tag.artist} - {title}.png')
        #plt.savefig(rf'C:\Users\serio\classical music\random\{tag.title}.png')
        print(i, end= ', ')

    except OSError:
        print('Error: ', end='')
        print(i, end=', ')
        continue

    except MemoryError:
        print('Error: ', end='')
        sleep(30)
        print(i, end=', ')
        continue

print()
print('All files graphs converted succesfully! ')








