import pandas as pd

data = pd.read_csv(r"C:\Users\serio\OneDrive\Escritorio\music.csv", index_col=None, na_values=['NA'])
data_1 = pd.read_csv(r"C:\Users\serio\OneDrive\Escritorio\music.csv", index_col=None, na_values=['NA'])

'''
Extract what interest us:

# Numerical data
songDuration = data['song.duration']
songTempo = data['song.tempo']
songYear = data['song.year']
songLoudness = data['song.loudness']
songHotness = data['song.hotttnesss']



# Text data
artistName = data['artist.name']
artistSimilar= data['artist.similar']
artistTerms = data['artist.terms']
songTitle = data['song.title']
'''

numerical = ['song.duration', 'song.tempo', 'song.year', 'song.loudness', 'song.hotttnesss']
text = ['artist.name', 'artist.similar', 'artist.terms', 'song.title']


for key, value in data.iteritems():

    if key not in numerical:
        data.drop(key, axis=1, inplace=True)

for key, value in data_1.iteritems():

    if key not in text:
        data_1.drop(key, axis=1, inplace=True)


data.to_csv('numerical_input.csv', sep=',')
data_1.to_csv('text_input.csv', sep=',')
