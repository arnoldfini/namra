from form import *
import pandas as pd
import csv
import os

'''

Loop through the songs till find its YT url thanks to Song's class declared in form.py

'''

data = pd.read_csv(r'C:\Users\serio\PycharmProjects\namra\dataset-manipulation\songsyt_url.csv', encoding="ISO-8859-1", index_col=None, na_values=['NA'])

song = []
urls = []

for i in range(len(data)):

    if data['url'][i] != 'ERROR!':

        song.append(data['name'][i])
        urls.append(data['url'][i])

print(song)
print(urls)

data.to_csv('def_songsyt_url.csv', sep=',')

exit(0)

songs = pd.read_csv(r'C:\Users\serio\PycharmProjects\namra\dataset-manipulation\songsyt.csv', index_col=None, na_values=['NA'], encoding="ISO-8859-1")

with open(r'C:\Users\serio\PycharmProjects\namra\dataset-manipulation\songsyt_url.csv', 'w') as f:

    writer = csv.writer(f)

    i = 0

    print('Copying csv file')

    for k, v in songs.iterrows():

        item = Song(v[1], v[0])

        link = item.yturl

        writer.writerow([songs['artist'][i], songs['name'][i], link])

        print(f'{i}/{len(songs)}')

        i += 1




