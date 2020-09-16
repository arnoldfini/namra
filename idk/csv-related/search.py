import pandas as pd

songs = pd.read_csv('songs.csv', index_col=None, na_values=['NA'])

for i in range(len(songs)):
    if songs['song.artist'][i] == 'Soda Stereo':
        print(songs['song.name'][i])