import pandas as pd

'''
File to grab the input.
Input: numerical atributes of songs used in the form stored in music.csv

Two types of input:

- Numerical (numerical values)

- Textual (every word is a dimension in itself)

'''

df = pd.read_csv(r'C:\Users\serio\PycharmProjects\neurontest\csv-related\songs.csv', index_col=None, na_values=['NA'], delimiter=',', encoding="utf-8-sig")


# NUMERICAL INPUT
