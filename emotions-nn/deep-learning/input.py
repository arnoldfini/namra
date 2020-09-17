import pandas as pd
from avgdata import getTitles

# Set input_real, the actual labels, to the titles themselves
input_real = getTitles()

'''
File to grab the input.
Input: numerical atributes of songs used in the form stored in music.csv

Two types of input:

- Numerical (numerical values)

- Textual (every word is a dimension in itself)

'''

df = pd.read_csv(r'D:\\fma_metadata\\raw_tracks.csv', index_col=None, na_values=['NA'], delimiter=',', encoding="utf-8")


# NUMERICAL INPUT
print(df)