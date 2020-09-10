import matplotlib as plt
import numpy as np
import pandas as pd
from emotions import *

'''

This file serves the purpose of processing the information in human-form.csv in a way a machine can comprehend.
Ergo changing Yes, No to 1, 0 respectively.

'''

def main():

    df = pd.read_csv(r'C:\Users\serio\PycharmProjects\namra\form-data\human-form.csv', encoding='utf-8', na_values=['NA'], header=None)
    columns = range(len(df.columns))

    column_names = [key for key, value in df.iteritems()]
    first_row = [value[0] for key, value in df. iteritems()]
    second_row = [value[1] for key, value in df.iteritems()]

    first_column = [df[0][i] for i in range(len(df))]


    '''
    
    Dictionaries below are where the emotions and its 2D location are stored
    Firstly, translate every spanish word in the csv to its respective feeling in english
    When in english, convert it into 2D vector
    
    '''

    # Else:
    #iterstrdf(df, key)

    print(df.head)


    for key in column_names:
        df[key] = np.where(df[key].eq('Sí'), 1,
                      np.where(df[key].eq('No'), 0,
                               np.where(df[key].isna(), 'NaN',
                                        np.where(df[key] not in first_row or second_row or first_column,
                                                 iterstrdf(df, key)
                                                 )
                                        )
                               )
                      )

    df.to_csv('machine-form.csv', sep=',')

    exit(100)

    # Rows
    for i in range(2, len(df)):

        # Columns
        for j in range(1, columns):

            if df[j][i] == 'Sí':

                df[j][i]

            elif df[j][i] == 'No':

                df[j][i] = 0

            elif df[j][i] == 'nan' or 'NaN':
                pass

            else:
                atrib = iterstr(df[j][i])

                print(atrib)

                for z in range(len(atrib)):
                    eng = emoarr[atrib[z]]
                    atrib[z] = emotovector[eng]
                    print(atrib[z])



    df.to_csv('machine-form.csv', sep=',')

def iterstrdf(df, key):

    # english - spanish
    emoinesp = emoreversetrans()
    # english - 2D vector
    emotovector = emodict()

    # Array where feelings in spanish are stored to compare if in csv
    # spanish - english
    emoarr = [k for k, v in emoinesp.items()]

    for i in range(len(df)):

        print(df[key][i])

        atrib = iterstr(df[key][i])

        for z in range(len(atrib)):

            eng = emoarr[atrib[z]]

            atrib[z] = emotovector[eng]



        iterstrdf(df, key)

        return atrib




def iterstr(string):

    # Value to check wether it has iterated a comma before
    value = 0

    # Array to store multiple atributes that are in a single cell
    atrib = []

    # Function only works if there is a comma to separate words, otherwise it returns the input (because there is only one word)
    try:

        for i in range(len(string)):

            if string[i] == ',' and value == 0:

                atrib.append(string[:i])

                tmp = i

                value += 1

            elif string[i] == ',' and value >= 1:

                atrib.append(string[tmp + 2:i])

                tmp = i

        atrib.append(string[tmp+2:len(string)])

        return atrib

    except:

        atrib.append(string)

        return atrib

main()
