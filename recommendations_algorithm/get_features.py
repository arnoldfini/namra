import pandas as pd
import numpy as np

def extract_features(ids):
    features_df = pd.read_csv(r'D:\fma_metadata\features.csv', index_col=0, na_values=['NA'], encoding='utf-8', header=[0, 1, 2])
    order = features_df.columns
    return features_df.loc[ids, order].round(6).to_numpy()

def features_dataset():
    def random_id_get():

        df = pd.read_csv(r'D:\fma_metadata\tracks.csv', index_col=None, na_values=['NA'], delimiter=',', encoding="utf-8")

        random_id = []
        random_titles = []
        random_artists = []

        for i in range(5, 105):
            random_titles.append(df['track.19'][i])
            random_artists.append(df['artist.11'][i])

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

