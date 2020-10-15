import ast
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import statistics as stat
import sys
from scipy.stats import norm
import scipy.stats as stats
from matplotlib import cm
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import Axes3D
import pylab as pl
import pandas as pd

df = pd.read_csv(r'C:\Users\serio\PycharmProjects\namra\form-related\form-data\machine-form.csv', encoding='utf-8',
                 header=[0, 1], index_col=None, na_values=['NA'])


def mu_sigma(song, df):
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

    square = np.asarray(square_avg(song, df))
    arithmetic = np.asarray(arithmetic_avg(song, df))

    # Return mu and sigma
    return arithmetic, np.sqrt(square - arithmetic ** 2)


def quartiles_median(song, trans):
    i = 0
    for key, value in df.iteritems():
        if key[0] == song and trans == 0:
            break

        elif key[0] == f'{song}.1' and trans == 1:
            break

        i += 1

    form = np.transpose(np.asarray(df))
    question = form[i]

    data = []

    if trans == 0:
        for key in question:
            if type(key) != type(2.1):
                tuples = ast.literal_eval(key)

                num0 = tuples[0]

                if type(num0) == type((3, 1)):
                    angle0 = data.append(np.degrees(np.arccos(num0[0])))
                    angle1 = data.append(np.degrees(np.arccos(num0[1])))

                else:
                    angle0 = data.append(np.degrees(np.arccos(num0)))

    elif trans == 1:
        for key in question:
            if type(key) != type(2.1):
                data.append(key)

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


def normal_graph(song):
    # Define mu and sigma
    _, _, _, data = quartiles_median(song, 0)

    # Azalea

    # weekend
    print(f'{song}: {data}')

    mu = np.mean(data)
    sigma = np.std(data)

    # Plot histogram
    plt.hist(data, bins=25, density=True, alpha=0.6, color='g')

    # Plot normal distribution
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, sigma)
    plt.plot(x, p, 'k', linewidth=2)

    plt.xlabel('Angle en º')
    plt.ylabel('Distribució Normal(x)')
    plt.title(f'Distribució Normal de {song} (' + '\u03BC =' f'{round(mu, 3)},' + ' \u03C3 =' f'{round(sigma, 3)})')

    return plt.show()


def normal_graph3d(song):
    # Data
    _, _, _, data1 = quartiles_median(song, 0)
    _, _, _, data2 = quartiles_median(song, 1)

    # Sample parameters
    mu = np.array([np.mean(data1), np.mean(data2)])
    sigma = np.array([[np.std(data1), np.std(data1)], [np.std(data2), np.std(data2)]])
    rv = multivariate_normal(mu, sigma)
    sample = rv.rvs(500)

    # Bounds parameters
    x_abs = 2.5
    y_abs = 2.5
    x_grid, y_grid = np.mgrid[-x_abs:x_abs:.02, -y_abs:y_abs:.02]

    pos = np.empty(x_grid.shape + (2,))
    pos[:, :, 0] = x_grid
    pos[:, :, 1] = y_grid

    levels = np.linspace(0, 1, 40)

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Removes the grey panes in 3d plots
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

    # The heatmap
    ax.contourf(x_grid, y_grid, 0.1 * rv.pdf(pos),
                zdir='z', levels=0.1 * levels, alpha=0.9)

    # The wireframe
    ax.plot_wireframe(x_grid, y_grid, rv.pdf(
        pos), rstride=10, cstride=10, color='k')

    # The scatter. Note that the altitude is defined based on the pdf of the
    # random variable
    ax.scatter(sample[:, 0], sample[:, 1], 1.05 * rv.pdf(sample), c='k')

    ax.legend()
    ax.set_title("Gaussian sample and pdf")
    ax.set_xlim3d(-x_abs, x_abs)
    ax.set_ylim3d(-y_abs, y_abs)
    ax.set_zlim3d(0, 1)

    return plt.show()

normal_graph('Weekend Warrior')
normal_graph('Bwar')
normal_graph('Azalea Waltz')



