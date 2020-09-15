import pandas as pd
from emotions import *
import numpy as np
import numpy.linalg as la
import math
from avgdata import getTitles, df_avg

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

df = df_avg()
emotions = emodict()
titles = getTitles
emotions_list = [k for k, v in emotions.items()]

'''
Identify feeling with song
'''
# First map the average feelings into the f( (x,y) ) = cos( (x,y) ) + i·sin( (x,y) )
mapping_avg = []

first_value = 0
second_value = 0

for i in range(len(df)):
    vector = df['Feelings'][i]
    mapping_avg.append(np.round(vector, decimals=2))
    
mapping_avg = np.array(mapping_avg)
mapping_avg_2d = []

# Compare form average feelings and find the most suitable
most_accurate = []

for i in range(len(mapping_avg)):

    round_error = []

    for key, value in emotions.items():

        input_vector = mapping_avg[i] @ np.array([1, 1], dtype=float)
        feeling_vector = value @ np.array([1, 1], dtype=float)
        result = feeling_vector - input_vector

        round_error.append(result)

    most_accurate_index = round_error.index(find_nearest(round_error, 0.))
    most_accurate_emotion = emotions_list[most_accurate_index]

    most_accurate.append(most_accurate_emotion)


print(f'Array mapping_avg_2d: {most_accurate}')
print(f'Length: {len(most_accurate)}')
