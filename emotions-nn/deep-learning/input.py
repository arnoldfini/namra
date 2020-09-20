import pandas as pd
from avgdata import getTitles
import numpy as np
import sys

# Set input_real, the actual labels, to the titles themselves
input_real = getTitles()

'''
File to grab the input.
Input: numerical attributes of songs used in the form stored in music.csv

Two types of input:

- Numerical (numerical values)

- Textual (every word is a dimension in itself)

'''


def get_id():
    titles = getTitles()
    df = pd.read_csv(r'D:\fma_metadata\tracks.csv', index_col=None, na_values=['NA'], delimiter=',', encoding="utf-8")
    id = []

    for song in titles:
        for i in range(len(df)):
            if song == df['track.19'][i]:
                id.append(df['Unnamed: 0'][i])
                break

    print(f'Titles: {titles} \nArray of IDs: {id} \nLength of the array {len(id)} ')

    return id


def extract_features(id_arr):
    features_df = pd.read_csv(r'D:\fma_metadata\features.csv', index_col=0, na_values=['NA'], encoding='utf-8')
    features = np.array(features_df.columns)

    id_arr = list(id_arr)

    for i in range(len(id_arr)):

        row_features = []

        for key, value in features_df.iteritems():
            row_features.append(round(float(features_df[key][int(id_arr[i])]), 6))

        row_features = np.asarray(row_features)
        features = np.vstack((features, row_features))

    features = np.delete(features, 0, 0)

    return features
