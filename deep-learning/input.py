import pandas as pd
from emotions import *
import numpy as np
import math
from avgdata import getTitles, df_avg

df = df_avg()
emotions = emodict()

'''
Identify feeling with song
'''
# First map the average feelings into the f( (x,y) ) = cos( (x,y) ) + i·sin( (x,y) )
mapping_avg = []

for i in range(len(df)):
    vector = df['Feelings'][i]
    mapping = lambda vector: [math.cos(vector[0]), math.sin(vector[1])]
    mapping_avg.append(np.round(mapping(vector), decimals=10))

mapping_avg = np.array(mapping_avg)

mapping_avg_2d = []

counter = 0
# Compare form average feelings and find the most suitable
for key, value in emotions.items():
    for i in range(len(mapping_avg)):
        if value == mapping_avg[i]:
            counter += 1
            mapping_avg_2d.append(key)

        elif counter < i:
            mapping_avg_2d.append('404')

print(mapping_avg_2d)








