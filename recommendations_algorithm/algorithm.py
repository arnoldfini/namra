from recommendations_algorithm.input_related.psico import Psychology
#from df_scrap import df_for_recommendation
from emotions import *
import pandas as pd
from time import sleep
import random
from selenium import webdriver
import re

name = input("\nCom et dius? ")

#df = df_for_recommendation()
df = pd.read_csv('df.csv', header=0, index_col=None, na_values=['NA'])

print('\nNon Archetypical Music Algorithm.\n')
print(f'Hola, {name}')
print('Per tal de recomanar-te les cançons més adequades, necessitem una mica de context. ')
print('Siusplau, respon a la següent pregunta.\n')

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

emoreverse = emocat_reverse()
emo_dict = emocat()
columns = len(df.columns)

print('-' * 50)
print(f"\nInforme de context de l'usuari:\nTemps: {weather}º\nEmoció: {emoreverse[emotion], emotion}\nHora del dia: {time}")
time = time / 24


def recommendation_algorithm(name, df, song_ids, emotion, weather, climate, time):
    suitable = []

    # Hot climate, cold weather -> - acousticness, + energy and danceability
    if climate == 0 and weather < 20:
        for i in range(len(df)):

            # Bad mood case, low intensity
            if emotion[0] < 0. and time > 20:
                if df['acousticness'][i] > 0.5 and (df['danceability'][i] and df['energy'][i] < 0.5):
                    if df['emotion_cos'][i] < 0. and df['emotion_sin'][i] < 0.:
                        suitable.append(df['track_id'][i])

            # Bad mood case, high intensity
            elif emotion[0] < 0. and time < 20:
                if df['acousticness'][i] > 0.5 and (df['danceability'][i] and df['energy'][i] < 0.5):
                    if df['emotion_cos'][i] < 0. and df['emotion_sin'][i] > 0.:
                        suitable.append(df['track_id'][i])

            # Good mood, low intensity
            elif emotion[0] > 0. and time > 20:
                if df['acousticness'][i] > 0.5 and (df['danceability'][i] and df['energy'][i] < 0.5):
                    if df['emotion_sin'][i] < 0. and df['emotion_cos'][i] > 0.:
                        suitable.append(df['track_id'][i])

            # Good mood, high intensity
            elif emotion[0] > 0. and time < 20:
                if df['acousticness'][i] > 0.5 and (df['danceability'][i] and df['energy'][i] < 0.5):
                    if df['emotion_sin'][0] > 0. and df['emotion_cos'][i] > 0.:
                        suitable.append(df['track.id'][i])

    # Cold climate, cold weather -> + acousticness, - energy and danceability
    elif climate == 1 and weather > 20:
        for i in range(len(df)):

            # Bad mood case, low intensity
            if emotion[0] < 0. and time > 20:
                if df['acousticness'][i] < 0.5 and (df['danceability'][i] and df['energy'][i] > 0.5):
                    if df['emotion_cos'][i] < 0. and df['emotion_sin'][i] < 0.:
                        suitable.append(df['track_id'][i])

            # Bad mood case, high intensity
            elif emotion[0] < 0. and time < 20:
                if df['acousticness'][i] < 0.5 and (df['danceability'][i] and df['energy'][i] > 0.5):
                    if df['emotion_cos'][i] < 0. and df['emotion_sin'][i] > 0.:
                        suitable.append(df['track_id'][i])

            # Good mood, low intensity
            elif emotion[0] > 0. and time > 20:
                if df['acousticness'][i] < 0.5 and (df['danceability'][i] and df['energy'][i] > 0.5):
                    if df['emotion_sin'][i] < 0. and df['emotion_cos'][i] > 0.:
                        suitable.append(df['track_id'][i])

            # Good mood, high intensity
            elif emotion[0] > 0. and time < 20:
                if df['acousticness'][i] < 0.5 and (df['danceability'][i] and df['energy'][i] > 0.5):
                    if df['emotion_sin'][0] > 0. and df['emotion_cos'][i] > 0.:
                        suitable.append(df['track.id'][i])

    if len(suitable) == 0:
        print("\nNo tenim cap cançó per recomanar-te en la nostra base de dades. Disculpes, en breus estarà arreglat.")
        sleep(1)
        print(f"\nEsperem veure't aviat, {name}! ")
        exit(0)

    suitable_title = []
    for i in range(len(suitable)):
        for j in range(len(song_ids)):
            if song_ids['track_id'][j] == suitable[i]:
                suitable_title.append(song_ids['track_title'][j])

    print()
    print('-'*50)
    print('\nNon Archetypical Music Algorithm en acció', end='')
    sleep(2)
    print('.', end='')
    sleep(2)
    print('.', end='')
    sleep(2)
    print('.\n')

    sleep(1)

    print(f"Llista de cançons adequades que l'algorisme et recomana, {name}: ")
    for song in suitable_title:
        print(f'- {song}')

    return


recommendation_algorithm(name, df, ids, emotion, weather, climate, time)
