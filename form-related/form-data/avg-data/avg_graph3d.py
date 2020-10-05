import matplotlib.pyplot as plt
from numpy.random import random
from avgdata import df_avg, getTitles
import math
from mpl_toolkits.mplot3d import Axes3D
from emotions import *

# Dataframe, and songs' titles
df = df_avg()
titles = getTitles()
emotions = emodict()
emotrans = emodictrans()

# Array where all the coordinates and its respective labels will be stored
x_values = []
y_values = []
z_values = []
actual_titles = []

# Declare "graph"
fig = plt.figure()
ax = plt.subplot(111, projection='3d')

# Axis names
ax.set_xlabel('Positivitat [cos(x)]', fontsize=10)
ax.set_ylabel('Intensitat [sin(x)]', fontsize=10)
ax.set_zlabel('Trascendent', fontsize=10)

# Random values declared in avg_graph.py, so they have the same plots.
random_values = [12, 34, 30, 14, 24, 26, 19, 26, 25, 32, 34, 1, 15, 35, 18, 32, 12, 27, 24, 13]

# Loop iterating through de dataframe to store each value to its respective coordinate (x,y or z)
for i in random_values:
    x_values.append(df['Feelings'][i][0])
    y_values.append(df['Feelings'][i][1])
    z_values.append(df['Transcendent'][i])
    actual_titles.append(titles[i])

# Plot the values, using the three arrays
ax.scatter(x_values, y_values, z_values)

# Name each point
for x, y, z, label in zip(x_values, y_values, z_values, actual_titles):
    ax.text(x, y, z, label)

# Move left y-axis and bottom x-axis to center of the figure
ax.plot((0, 0), (-1, 1), 'k--')
ax.plot((-1, 1), (0, 0), 'k--')

# UNIT CIRCLE PLOT
sin = []
cos = []

# Append all values so they form an unit circle
for i in range(0, 360):
    cos.append(math.cos(i))
    sin.append(math.sin(i))


# Plot unit circle
ax.plot(cos, sin, 'k--', linewidth=0.1)

zeros = []

for key, value in emotions.items():
    zeros.append(0)

# Label the emotions in a 2D plane, which they lie in the unit circle
for key, value in emotions.items():
    plt.annotate(emotrans[key], value, zeros)

# Draw emotion points
plt.scatter([v[0] for k, v in emotions.items()], [v[1] for k, v in emotions.items()], zeros, c='k')

# Title and show
plt.title('Emocions entre cançons')
plt.show()
