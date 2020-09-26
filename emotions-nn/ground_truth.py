from emotions import emodict
import numpy as np
from avgdata import getTitles, df_avg


def compute_ground_truth(df):

    def find_nearest(array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return array[idx]

    emotions = emodict()
    emotions_list = [k for k, v in emotions.items()]
    titles = getTitles()

    '''
    Identify feeling with song
    '''

    mapping_avg = []

    for i in range(len(df)):
        vector = df['Feelings'][i]
        mapping_avg.append(np.round(vector, decimals=2))

    mapping_avg = np.array(mapping_avg)

    # Compare form average feelings and find the most suitable
    most_accurate = []

    for i in range(len(mapping_avg)):
        round_error = []

        for key, value in emotions.items():
            input_vector = mapping_avg[i] @ np.array([1, 1], dtype=float)
            feeling_vector = value @ np.array([1, 1], dtype=float)
            result = feeling_vector - input_vector

            round_error.append(result)

        most_accurate_index = round_error.index(find_nearest(round_error, 0.))
        most_accurate_emotion = emotions_list[most_accurate_index]

        most_accurate.append(most_accurate_emotion)

    # Transform feelings into vectors as its own dimension
    emotions = emodict()
    emotions_list = [k for k, v in emotions.items()]

    ground_truth = np.zeros((len(most_accurate), len(emotions)), dtype=int)

    for i in range(len(most_accurate)):
        for j in range(len(emotions_list)):
            if most_accurate[i] == emotions_list[j]:
                index = emotions_list.index(emotions_list[j])

                ground_truth[i][index] = 1

    return ground_truth


