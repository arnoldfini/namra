import pandas as pd
import csv

df = pd.read_csv(r'C:\Users\serio\PycharmProjects\namra\form-data\machine-form.csv', encoding='utf-8')

titles = []

with open('titles.txt', 'r') as f:

    read = csv.reader(f, delimiter=' ', quotechar='|')

    for song in read:

        titles.append(song)

newtitles = [song for song in titles[0]]
titles = newtitles