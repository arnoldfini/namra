import csv
import pandas as pd
import numpy as np

'''
Extract titles from titles.txt
'''

titles = []

with open('../form-data/avg-data/titles.txt', 'r') as f:

    read = csv.reader(f, delimiter=',', quotechar='|')

    for song in read:

        titles.append(song)

newtitles = [song for song in titles[0]]
titles = newtitles

'''
Search for the average attributes of each song

Information taken into account:

- Feeling they had when listening
- If they made them reflect
'''

df = pd.read_csv(r'/form-data/machine-form.csv', encoding='utf-8', header=0)  # Header ?

# Relevant columns
rel_columns = ['¿Cómo te has sentido durante la canción?', '¿Crees que la canción incita a la reflexión?']

# 2D array to store all the songs with its respective avg
avg = []
nums = np.empty((len(titles), 2*len(df.columns)), dtype=str)

for i in range(len(titles)):
    nums[i][0] = titles[i]

#context_headers = ['Unnamed: 0', 'Timestamp', '¿Resides en España?', '¿En qué país entonces?', 'Selecciona el lugar más cercano a tu residencia.', '¿Cómo dirías que te sientes ahora mismo?', 'Selecciona una casilla aleatoria']

for i in range(1, len(df)):

    for key, value in df.iteritems():

        if type(df[key][i]) != type(float):

            try:
                # If there's a num after the column name, it gets stored in 'end'. So index > 0
                row = int(key[len(key)-1])

                if key.startswith('¿Cómo'):
                    nums[row][1] = df[key][i]

                else:
                    nums[row][2] = df[key][i]

            except:
                # Otherwise, if there's an error, means it's actually a string. So index == 0
                if key.startswith('¿Cómo'):
                    nums[0][1] = df[key][i]

                else:
                    nums[0][2] = df[key][i]

        else:

            continue

#with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also

with open('../form-data/avg-data/describe.txt', 'w') as f:
    describe = str(df.describe().to_string())
    f.write(describe)


'''# First song: titles[0]

for i in range(len(df)):

    if type(df[rel_columns[0] + f'.{i}'][i]) == type(float):

        nums[i][0] = 0

    if type(df[rel_columns[1] + f'.{i}'][i]) == type(float):



    if i != 0:


        nums[i][0] = tuple(df[rel_columns[0] + f'.{i}'][i])
        nums[i][1] = int(df[rel_columns[0] + f'.{i}'][i])

    else:

        nums[i][0] = tuple(df[rel_columns[0]][i])
        nums[i][1] = int(df[rel_columns[1]][i])

print(nums)

'''
