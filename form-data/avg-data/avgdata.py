import csv
import pandas as pd
import numpy as np
import numpy.linalg as la

'''
Functions
'''


def iter_str_tuple(tuple_str):
    attributes = np.array([0, 0], dtype=float)

    if tuple_str.startswith('('):
        tuple_str = tuple_str[1:]

    if tuple_str.endswith(')'):
        tuple_str = tuple_str[:len(tuple_str) - 1]

    for i in range(len(tuple_str)):

        if tuple_str[i] == ',':
            attributes[0] = float(tuple_str[:i])
            attributes[1] = float(tuple_str[i + 1:])

    return attributes


'''
Extract titles from titles.txt
'''
def getTitles():
    titles = []

    with open('titles.txt', 'r') as f:
        read = csv.reader(f, delimiter=',', quotechar='|')

        for song in read:
            titles.append(song)

    newtitles = [song for song in titles[0]]
    titles = newtitles

    return titles

titles = getTitles()

'''
Search for the average attributes of each song

Information taken into account:

- Feeling they had when listening (vector)
- If they made them reflect (integer)
'''

df = pd.read_csv(r'C:\Users\serio\PycharmProjects\namra\form-data\machine-form.csv', encoding='utf-8', header=1)

# Array to store only the
nums = np.empty((1, len(df.columns)), dtype=int)
avg = []

context_headers = ['Unnamed: 0',
                   'Timestamp',
                   '¿Resides en España?',
                   '¿En qué país entonces?',
                   'Selecciona el lugar más cercano a tu residencia.',
                   '¿Cómo dirías que te sientes ahora mismo?',
                   'Selecciona una casilla aleatoria']

key_num = 0
for key, value in df.iteritems():

    if key in context_headers:
        continue

    suma = 0
    vector_suma = np.array([0, 0], dtype=float)
    counter = 0

    for i in range(len(df)):
        try:
            if type(np.float64()) == type(value[i]):
                suma += int(value[i])
                counter += 1

            elif value[i].endswith(')'):
                vector_suma += iter_str_tuple(value[i])
                counter += 1

        except ValueError:
            continue

        except AttributeError:
            continue

    if la.norm(vector_suma) == la.norm(np.array([0, 0], dtype=float)):
        avg.append(round(suma / counter))

    else: # if suma == 0:
        avg.append(np.round(vector_suma / counter, decimals=10))



    key_num += 1


def df_avg():

    df_dict = {'Feelings': [avg_feeling for avg_feeling in avg[::3]],
               'Transcendent': [avg_transc for avg_transc in avg[1::3]],
               'Likeable': [like for like in avg[2::3]]}

    avg_df = pd.DataFrame(df_dict, columns=['Feelings', 'Transcendent', 'Likeable'], index=[song for song in titles])

    return avg_df


#with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
