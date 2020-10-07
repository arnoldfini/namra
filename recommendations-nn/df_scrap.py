import pandas as pd
import numpy as np
from avgdata import getTitles
from get_features import features_dataset
import emotions_nn.test_model as model


def df_for_recommendation():
    df = pd.read_csv(r'D:\fma_metadata\echonest.csv', index_col=0, header=2, na_values=['NA'], delimiter=',',
                     encoding="utf-8")

    columns = ['acousticness', 'danceability', 'energy']  # 'artist_latitude' 'artist_longitude'
    df = df.reindex(columns=columns)
    df.drop(df.index[101:], inplace=True)

    features, titles, _ = features_dataset()
    emotions = []

    for i in range(len(features)):
        emotions.append(model.predict_emotions(features[i]))

    cos = [val[0] for val in emotions]
    sin = [val[1] for val in emotions]
    cos.insert(0, 'NaN')
    sin.insert(0, 'NaN')

    df.insert(3, 'emotion_cos', cos, True)
    df.insert(4, 'emotion_sin', sin, True)

    # input_df = new_df.loc[new_df.index.intersection(ids)].round(6).to_numpy()
    # print(input_df)

    return df
