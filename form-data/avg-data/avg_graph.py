import matplotlib.pyplot as plt
from avgdata import df_avg, getTitles
from emotions import emodict, emodictrans
import numpy as np

# Declare Dataframe, titles, and emotions dictionaries
df = df_avg()
titles = getTitles()
emotions = emodict()
emotrans = emodictrans()

# Array where all the coordinates and its respective labels will be stored
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

#  Unit circle
ax = fig1.add_subplot(1, 1, 1)
circ = plt.Circle((0, 0), radius=1, edgecolor='k', facecolor='None')
ax.add_patch(circ)

# Array to store transcendent, and no transcendent, so we can put a legend on the first one.
trans_songs = [[], []]
no_trans_songs = [[], []]

# Array to store the random values if useful later
random_values = [12, 34, 30, 14, 24, 26, 19, 26, 25, 32, 34, 1, 15, 35, 18, 32, 12, 27, 24, 13]
i=0
for j in random_values:
#for i in range(len(df)):

    # Create random number to iterate random rows in the dataframe, and store it in random_values[]
    #j = int(len(df) * np.random.random_sample())
    #random_values.append(j)

    # Append both x and y coordinates
    x_values.append(df['Feelings'][j][0])
    y_values.append(df['Feelings'][j][1])

    # However, if column df['Transcendent'][j] is 1, the colour must be read, so it's distinguishable
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
    i+=1

# Draw points
plt.scatter(trans_songs[0], trans_songs[1], c='r', label='Música trascendent')
plt.scatter(no_trans_songs[0], no_trans_songs[1], label='Música no trascendent')

# Legend the labels above
plt.legend(loc='upper left',
          fancybox=True, shadow=True, ncol=1)

# Label the emotions in a 2D plane, which they lie in the unit circle
for key, value in emotions.items():
    plt.annotate(emotrans[key], value)

# Draw emotion points
plt.scatter([v[0] for k, v in emotions.items()], [v[1] for k,v in emotions.items()], c='k')
plt.scatter(x_values, y_values, c=colour_sequence)

# Name axis
plt.xlabel('Positivitat [cos(x)]')
plt.ylabel('Intensitat [sin(x)]')

plt.title('Emocions entre cançons ')
plt.show()
