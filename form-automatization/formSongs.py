from form import *

songs = pd.read_csv(r'C:\Users\serio\PycharmProjects\namra\dataset-manipulation\songsyt.csv', index_col=None, na_values=['NA'])

with open(r'C:\Users\serio\PycharmProjects\namra\dataset-manipulation\songsyt+url.csv') as f:

    writer = csv.writer(f)

    for k, v in songs:

        item = Song(v[0], v[1])

        writer.writerow([songs['Newagehillbilly'][k], songs['Weekend Warrior'][k], item.url])



