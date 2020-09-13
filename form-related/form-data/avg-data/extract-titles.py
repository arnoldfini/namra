import pandas as pd
import csv

'''

Extract titles (song names) from human-form.csv

'''

df = pd.read_csv(r'C:\Users\serio\PycharmProjects\namra\form-data\human-form.csv', encoding='utf-8', header=None)

titles = []
tmp = 'Some variable'

for key, value in df.iteritems():

    if key == 0:

        tmp = value[0]

    else:

        if value[0] != tmp and value[0] != 'USER.CONTEXT':

            titles.append(value[0])

            tmp = value[0]

        else:

            tmp = value[0]



with open(r'titles.txt', 'w+') as f:

    w = csv.writer(f)

    w.writerow(titles)