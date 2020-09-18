import pandas as pd
from avgdata import getTitles

# Set input_real, the actual labels, to the titles themselves
input_real = getTitles()

'''
File to grab the input.
Input: numerical attributes of songs used in the form stored in music.csv

Two types of input:

- Numerical (numerical values)

- Textual (every word is a dimension in itself)

'''

df = pd.read_csv(r'D:\fma_metadata\raw_tracks.csv', index_col=0, na_values=['NA'], delimiter=',', encoding="utf-8")
titles = getTitles()

repeated = []
for key, value in df.iterrows():

    if df['track_title'][key] in repeated:
        continue

    else:
        if df['track_title'][key] in titles:
            repeated.append(df['track_title'][key])

    for i in range(len(repeated)):
        for j in range(len(titles)):
            if repeated[i] != titles[i]:
                tmp_index = titles.index(titles[i])

                tmp = titles[i]

                for k in range(len(titles)):
                    if titles[k] == tmp:
                        titles[k], titles[tmp_index] = tmp, titles[k]

print(titles)

# NUMERICAL INPUT
print(df)
