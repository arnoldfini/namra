import pandas as pd
import csv
from time import sleep

# 1.

# Import csv database and extract 1000 songs

tracks = pd.read_csv(r'D:\fma_metadata\raw_tracks.csv', index_col=None, na_values=['NA'])


# Split the data multiple times so there is more variety
tracks.drop(tracks.index[::2], inplace=True)
tracks.drop(tracks.index[100000:], inplace=True)
tracks.drop(tracks.index[::2], inplace=True)
tracks.drop(tracks.index[::2], inplace=True)
tracks.drop(tracks.index[::2], inplace=True)
tracks.drop(tracks.index[::2], inplace=True)
tracks.drop(tracks.index[::2], inplace=True)
tracks.drop(tracks.index[::2], inplace=True)
tracks.drop(tracks.index[::2], inplace=True)
tracks.drop(tracks.index[::2], inplace=True)
tracks.drop(tracks.index[::2], inplace=True)

# Catch the first 100 songs
tracks.drop(tracks.index[100:], inplace=True)

# Save it to a .csv file
tracks.to_csv('1000tracks', sep=',')

sleep(5)


# 2.

# Import new csv and find 100 songs' names and artists to search its url

# Load csv with 100 tracks
tracks = pd.read_csv(r'C:\Users\serio\PycharmProjects\namra\dataset-manipulation\1000tracks', index_col=None, na_values=['NA'])

# Catch only the artist_name and track_title columns
imp = tracks[['artist_name', 'track_title']]

# Write a new csv file with all the information about title and artist
with open('songsyt.csv', 'w', newline='') as file:

    writer = csv.writer(file)

    for i in range(len(imp)):

        try:

            writer.writerow([imp["artist_name"][i], imp["track_title"][i]])

        except:

            continue



