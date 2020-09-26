import pandas as pd

# Df with information about if the person liked or disliked the song
df = pd.read_csv(r'namra\\form-related\\form-data\\machine-form.csv', header=1, index_col=None, na_values=['NA'])


likeness = np.array([], ndim=2, dtype=int)
for key, value in df.iteritems():

    nums = []
    avg = 0

    for i in range(len(df)):

        nums.append(df[key][i])

    # Sum all elements in the array
    avg = [avg += num for num in nums]

    # Actual average
    avg = round(avg/len(nums))

    likeness.append(avg)
