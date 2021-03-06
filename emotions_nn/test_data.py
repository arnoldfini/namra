import numpy as np
import pandas as pd
from avgdata import getTitles
# from input import extract_features


def extract_features(ids):
    features_df = pd.read_csv(r'D:\fma_metadata\features.csv', index_col=0, na_values=['NA'], encoding='utf-8', header=[0, 1, 2])
    order = features_df.columns
    return features_df.loc[ids, order].round(6).to_numpy()


def test_dataset():
    def random_id_get():

        df = pd.read_csv(r'D:\fma_metadata\tracks.csv', index_col=None, na_values=['NA'], delimiter=',', encoding="utf-8")

        random_id = []
        random_titles = []
        random_artists = []
        model_titles = getTitles()

        for i in range(36):
            j = np.random.randint(low=10, high=6000, dtype=int)
            random_titles.append(df['track.19'][j])
            random_artists.append(df['artist.11'][j])

        for song in random_titles:
            for i in range(len(df)):

                if song == df['track.19'][i]:
                    random_id.append(df['Unnamed: 0'][i])
                    break

        random_id = np.asarray(random_id, dtype=int)

        print(f'Titles: {random_titles} \nArray of IDs: {random_id} \nLength of the array {len(random_titles)} ')

        return random_id, random_titles, random_artists

    ids, random_titles, random_artists = random_id_get()

    return extract_features(ids), random_titles, random_artists
