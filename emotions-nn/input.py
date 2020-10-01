import pandas as pd
from avgdata import getTitles
import numpy as np
import sys

# Set input_real, the actual labels, to the titles themselves
input_real = getTitles()

'''
File to grab the input.
Input: numerical attributes of songs used in the form stored in music.csv

Input:

- Numerical (numerical values) from D:\fma_metadata\features.csv

'''


def get_id():
    # Iterate through the dataframe to store the song's IDs
    titles = getTitles()
    df = pd.read_csv(r'D:\fma_metadata\tracks.csv', index_col=None, na_values=['NA'], delimiter=',', encoding="utf-8")
    id = []

    for song in titles:
        for i in range(len(df)):
            if song == df['track.19'][i]:
                id.append(df['Unnamed: 0'][i])
                break

    id = np.asarray(id, dtype=int)

    print(f'Titles: {titles} \nArray of IDs: {id} \nLength of the array {len(id)}')

    return id


def extract_features(ids):
    features_df = pd.read_csv(r'D:\fma_metadata\features.csv', index_col=0, na_values=['NA'], encoding='utf-8', header=[0, 1, 2])
    order = features_df.columns
    return features_df.loc[ids, order].round(6).to_numpy()


