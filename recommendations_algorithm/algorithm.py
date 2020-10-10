from df_scrap import df_for_recommendation
from recommendations_algorithm.input_related.psico import Psychology
from emotions import *

# INPUT
user = Psychology()
weather = user.weather
emotion = user.emotion
time = user.time

df = df_for_recommendation()
emo_dict = emoreverse()
columns = df.columns
print(df)

print('-'*20)
print(f'\nUser context report:\nWeather: {weather}º\nEmotion: {emo_dict[emotion]}\nTime: {time}')
time = time/24


def recommendation_algorithm(emotion, weather, time):
    pass
