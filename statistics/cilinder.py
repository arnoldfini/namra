import matplotlib.pyplot as plt
import matplotlib as mat
import numpy as np
import emotions_nn.avgdata as avgdata
import math


df = avgdata.df_avg()
titles = avgdata.getTitles()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# UNIT CIRCLE PLOT
sin = []
cos = []
z = []

# Append all values so they form an unit circle
for i in range(0, 360):
    cos.append(math.cos(i))
    sin.append(math.sin(i))
    if i % 2 == 0:
        z.append(1)
    else:
        z.append(0)


# Plot unit circle
ax.plot(cos, sin,z, 'k--', linewidth=0.1)


# POINTS
X = df['Feelings'][34][0]
Y = df['Feelings'][34][1]
Z = df['Likeable'][34]


# Plot the surface.
#ax.scatter(X, Y, Z, titles[0])
#ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)

# Tweak the limits and add latex math labels.
ax.set_zlim(0, 1)
ax.set_xlabel('Positivitat')
ax.set_ylabel('Intensitat')
ax.set_zlabel('Trascendental')
plt.title(titles[34])
print(np.degrees(np.arccos(X)), end=' ')
print(Z)
plt.show()
