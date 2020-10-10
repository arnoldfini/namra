import ast
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import statistics as stat
import sys
from scipy.stats import norm
import scipy.stats as stats
import pylab as pl
import pandas as pd

df = pd.read_csv(r'C:\Users\serio\PycharmProjects\namra\form-related\form-data\machine-form.csv', encoding='utf-8',
                 header=[0, 1], index_col=None, na_values=['NA'])

'''def iter_str_tuple(tuple_str):
    attributes = np.array([0, 0], dtype=float)

    if tuple_str.startswith('('):
        tuple_str = tuple_str[1:]

    if tuple_str.endswith(')'):
        tuple_str = tuple_str[:len(tuple_str) - 1]

    for i in range(len(tuple_str)):

        if tuple_str[i] == ',':
            attributes[0] = float(tuple_str[:i])
            attributes[1] = float(tuple_str[i + 1:])

    return attributes[0], attributes[1]


def square_avg(song, df):
    nums_emotions_cos = []
    nums_emotions_sin = []
    nums_transcendental = []
    nums_like = []

    for i in range(1, len(df)):

        if type(df[f'{song}'][i]) != type(3.1):

            cos, sin = list(ast.literal_eval((df[f'{song}'][i])))
            print(cos)

        if type(df[f'{song}'][i]) != type(3.1):
            nums_transcendental.append(int(df[f'{song}.1'][i]) ** 2)

        if type(df[f'{song}'][i]) != type(3.1):
            nums_like.append(int(df[f'{song}.2'][i]) ** 2)

    # Average of each other:
    avg_cos = 0
    for i in range(len(nums_emotions_cos)):
        avg_cos += nums_emotions_cos[i]
    avg_cos = avg_cos / len(nums_emotions_cos)

    avg_sin = 0
    for i in range(len(nums_emotions_sin)):
        avg_sin += nums_emotions_sin[i]
    avg_sin = avg_sin / len(nums_emotions_sin)

    avg_trans = 0
    for i in range(len(nums_transcendental)):
        avg_trans += nums_transcendental[i]
    avg_trans = avg_trans / len(nums_transcendental)

    avg_like = 0
    for i in range(len(nums_like)):
        avg_like += nums_like[i]
    avg_like = avg_like / len(nums_like)

    return avg_cos, avg_sin, avg_trans, avg_like


def arithmetic_avg(song, df):
    nums_emotions_cos = []
    nums_emotions_sin = []
    nums_transcendental = []
    nums_like = []

    for i in range(1, len(df)):

        if type(df[f'{song}'][i]) != type(3.1):
            try:
                cos, sin = ast.literal_eval(df[f'{song}'][i])

            except KeyError:
                continue

        if type(df[f'{song}.1'][i]) != type(3.1):
            nums_transcendental.append(int(df[f'{song}.1'][i]))

        if type(df[f'{song}.2'][i]) != type(3.1):
            nums_like.append(int(df[f'{song}.2'][i]))

    # Average of each other:
    avg_cos = 0
    for i in range(len(nums_emotions_cos)):
        avg_cos += nums_emotions_cos[i]
    avg_cos = avg_cos / len(nums_emotions_cos)

    avg_sin = 0
    for i in range(len(nums_emotions_sin)):
        avg_sin += nums_emotions_sin[i]
    avg_sin = avg_sin / len(nums_emotions_sin)

    avg_trans = 0
    for i in range(len(nums_transcendental)):
        avg_trans += nums_transcendental[i]
    avg_trans = avg_trans / len(nums_transcendental)

    avg_like = 0
    for i in range(len(nums_like)):
        avg_like += nums_like[i]
    avg_like = avg_like / len(nums_like)

    return avg_cos, avg_sin, avg_trans, avg_like


def variance(song, df):
    square = np.asarray(square_avg(song, df))
    arithmetic = np.asarray(arithmetic_avg(song, df))
    return square - arithmetic ** 2


def standard_deviation(song, df):
    return np.sqrt(variance(song, df))
'''


def quartiles_median(song):
    i = 0
    for key, value in df.iteritems():
        if key[0] == song:
            break
        i += 1

    form = np.transpose(np.asarray(df))
    question = form[i]

    data = []
    for key in question:

        if type(key) != type(2.1):
            tuples = ast.literal_eval(key)

            num0 = tuples[0]

            if type(num0) == type((3, 1)):
                angle0 = data.append(np.degrees(np.arccos(num0[0])))
                angle1 = data.append(np.degrees(np.arccos(num0[1])))

            else:
                angle0 = data.append(np.degrees(np.arccos(num0)))

    data = np.asarray(sorted(data))
    data = np.round(data, decimals=0)
    data = np.asarray(data, dtype=int)
    data = data.tolist()

    q1 = np.percentile(data, 25)
    median = np.percentile(data, 50)
    q3 = np.percentile(data, 75)

    return q1, median, q3, data


def count_nums_in_array(array):
    # Function that returns occurrence of the items in array in a df (key, value)
    a = np.array(array)
    unique, counts = np.unique(a, return_counts=True)
    occurrence_items = dict(zip(unique, counts))

    x = [key for key, value in occurrence_items.items()]
    y = [value for key, value in occurrence_items.items()]

    df = pd.Series(occurrence_items, index=occurrence_items.keys())

    return df


song = 'Bwar'

# Define mu and sigma
_, _, _, data = quartiles_median(song)
#del data[len(data)-1]

mu = np.mean(data)
sigma = np.std(data)

# Plot histogram
plt.hist(data, bins=25, density=True, alpha=0.6, color='g')

# Plot normal distribution
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, sigma)
plt.plot(x, p, 'k', linewidth=2)

plt.title(f'Distribució Normal de {song} (' + '\u03BC =' f'{round(mu, 3)},' + ' \u03C3 =' f'{round(sigma, 3)})')
plt.show()

'''count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *
         np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)),
         linewidth=2, color='r')
plt.show()'''
