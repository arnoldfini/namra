import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.stats as stats

df = pd.read_csv(r'C:\Users\serio\PycharmProjects\namra\form-related\form-data\machine-form.csv', encoding='utf-8',
                 header=[0,1], index_col=None, na_values=['NA'])

print(df.head())


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

    return attributes[0], attributes[1]


def square_avg(song, df):
    nums_emotions_cos = []
    nums_emotions_sin = []
    nums_transcendental = []
    nums_like = []

    for i in range(1, len(df)):

        if type(df[f'{song}'][i]) != type(3.1):
            try:
                cos, sin = iter_str_tuple(df[f'{song}'][i])

                nums_emotions_cos.append(cos ** 2)
                nums_emotions_sin.append(sin ** 2)

            except ValueError:

                continue

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
                cos, sin = iter_str_tuple(df[f'{song}'][i])

                nums_emotions_cos.append(cos)
                nums_emotions_sin.append(sin)

            except ValueError:

                continue

        if type(df[f'{song}'][i]) != type(3.1):
            nums_transcendental.append(int(df[f'{song}.1'][i]))

        if type(df[f'{song}'][i]) != type(3.1):
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


s = df['Weekend Warrior']
standard_dev = np.std(s)
arith_avg = np.mean(s)

mu, sigma = arith_avg[1], standard_dev[1]
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.title('La volverías a escuchar?'+' \u03BC =' f'{round(mu, 3)},'+' \u03C3 =' f'{round(sigma, 3)}')
plt.show()


'''count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *
         np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)),
         linewidth=2, color='r')
plt.show()'''
