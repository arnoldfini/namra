import matplotlib.pyplot as plt
from avgdata import df_avg, getTitles
from emotions import emodict, emodictrans
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

df = df_avg()
titles = getTitles()
emotions = emodict()
emotrans = emodictrans()

x_values = []
y_values = []
colour_sequence = []



# Axis
fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)
ax1.set_xbound(-1,1)
ax1.set_ybound(-1,1)


# Move left y-axis and bottom x-axis to center of the figure
plt.plot((0, 0), (-1, 1), 'k--')
plt.plot((-1, 1), (0, 0), 'k--')

#   Unit circle
ax = fig1.add_subplot(1, 1, 1)
circ = plt.Circle((0, 0), radius=1, edgecolor='k', facecolor='None')
ax.add_patch(circ)

# Array to store transcendent, and no transcendent, so we can put a legend on the first one.
trans_songs = [[], []]
no_trans_songs = [[], []]

for i in range(20):

    j = int(len(df) * np.random.random_sample())

    x_values.append(df['Feelings'][j][0])
    y_values.append(df['Feelings'][j][1])

    if df['Transcendent'][j] == 1:
        colour_sequence.append('red')
        plt.annotate(titles[j], (x_values[i], y_values[i]))
        trans_songs[0].append(x_values[i])
        trans_songs[1].append(y_values[i])

    else:
        colour_sequence.append('blue')
        plt.annotate(titles[j], (x_values[i], y_values[i]))
        no_trans_songs[0].append(x_values[i])
        no_trans_songs[1].append(y_values[i])



plt.scatter(trans_songs[0], trans_songs[1], c='r', label='Música trascendent')
plt.scatter(no_trans_songs[0], no_trans_songs[1], c='b')
#plt.legend(legend_val, 'Trascendent', loc='lower left', ncol=3, fontsize=8, scatterpoints=1)
#plt.legend(handles=scatter.legend_elements()[0], labels='Trascendent')
plt.legend(loc='upper left',
          fancybox=True, shadow=True, ncol=4)

for key, value in emotions.items():
    plt.annotate(emotrans[key], value)

plt.xlabel('Positivitat [cos(x)]')
plt.ylabel('Intensitat [sin(x)]')



plt.title('Emocions entre cançons ')
plt.scatter(x_values, y_values, c=colour_sequence)
plt.show()
