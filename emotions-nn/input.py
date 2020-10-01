import pandas as pd
from avgdata import getTitles
import numpy as np
import sys

# Declarar input_real
input_real = getTitles()

'''

Fitxer per extreure l'input.
Input: valors numèrics de les cançons emmagatzemats a D:\fma_metadata\features.csv

'''


def get_id():
    # Iterar per tot el dataframe per emmagatzemar els IDs de les cançons desitjades
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


