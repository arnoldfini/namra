import tensorflow as tf
import keras
import pandas as pd
from ground_truth import get_ground_truth

'''
Document to track all useful data into one place
'''

data = pd.read_csv(r'D:\fma_metadata\raw_tracks.csv')

'''

Input

Attributes of each song in raw_tracks.csv in D:\\fma_metadata\\raw_tracks.csv'

'''

input_data =



'''

Ground truth

To compare current data with expected data to make the NN as accurate as possible

'''
ground_truth = get_ground_truth()
