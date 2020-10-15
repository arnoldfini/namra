from recommendations_algorithm.input_related.psico import Psychology
#from df_scrap import df_for_recommendation
from emotions import *
import pandas as pd
from time import sleep
import random
from selenium import webdriver
import re

name = input("\nWhat's your name? ")

#df = df_for_recommendation()
df = pd.read_csv('df.csv', header=0, index_col=None, na_values=['NA'])

print('\nNon Archetypical Music Algorithm. All rights reserved.\n')
print(f'Hello, {name}')
print('In order to recommend you the most suitable songs, we need a bit of context. ')
print('Please respond the following question.\n')

# INPUT
user = Psychology()
weather = user.weather
emotion = user.emotion
time = user.time
climate = 0

ids = pd.read_csv(r'D:\fma_metadata\raw_tracks.csv', header=0, na_values=['NA'])
columns_to_delete = list(ids.columns)
del columns_to_delete[0]
del columns_to_delete[36]
ids.drop(columns=columns_to_delete, inplace=True)
ids.drop(ids.index[101:], inplace=True)
#print(ids)

emo_dict = emoreverse()
columns = len(df.columns)

print('-' * 50)
print(f'\nUser context report:\nWeather: {weather}º\nEmotion: {emo_dict[emotion]}\nTime: {time}')
time = time / 24


def recommendation_algorithm(name, df, song_ids, emotion, weather, climate, time):
    suitable = []

    if climate == 0 and weather < 20:
        for i in range(len(df)):

            # Bad mood case, low temperature,
            if df['emotion_sin'][i] > 0. and df['emotion_cos'][i] < 0. and df['acousticness'][i] > 0.5 and (df['danceability'][i] and df['energy'][i] < 0.5):
                suitable.append(df['track_id'][i])

            # Bad mood case, high temperature (High intensity as for temp, low positivity as for mood)
            elif df['emotion_sin'][i] > 0. and df['emotion_cos'][i] < 0. and df['acousticness'][i] > 0.5 and (df['danceability'][i] and df['energy'][i] < 0.5):
                suitable.append(df['track_id'])

            # Good mood, low temperature
            # Good mood, high temperature

    suitable_title = []
    for i in range(len(suitable)):
        for j in range(len(song_ids)):
            if song_ids['track_id'][j] == suitable[i]:
                suitable_title.append(song_ids['track_title'][j])

    print()
    print('-'*50)
    print('\nNon Archetypical Music Algorithm in action', end='')
    sleep(2)
    print('.', end='')
    sleep(2)
    print('.', end='')
    sleep(2)
    print('.\n')

    sleep(1)

    if len(suitable_title) == 0:
        print("\nWe don't have any song to recommend you in our database. Apologies and will be fixed soon.")
        pass

    else:
        print(f'List of songs the algorithm recommends to you, {name}: ')
        for song in suitable_title:
            print(f'- {song}')



    sleep(1)
    print(f'Hope to see you soon {name}! ')

    return


recommendation_algorithm(name, df, ids, emotion, weather, climate, time)
