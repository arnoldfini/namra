import pandas as pd

musicdata = pd.read_csv(r'C:\Users\serio\PycharmProjects\neurontest\csv-related\music.csv', index_col=None, na_values=['NA'], delimiter=',', encoding="utf-8-sig")
songdata = pd.read_csv(r'C:\Users\serio\PycharmProjects\neurontest\csv-related\songs.csv', index_col=None, na_values=['NA'], delimiter=',', encoding="utf-8-sig")

print('Starting...')

print(musicdata)

for j in range(len(musicdata['song.id'][44000: 54000])):

    try:

        if j % 100000 == 0:
            print(j, end=', ')

        if str(musicdata['song.id'][i]) == str(songdata['song.id'][j]):

            musicdata['song.title'][i] = songdata['song.name'][j]
            songdata.drop(j, axis=0)

            print(f'Row {i} done, song was number {j}')

            print()

            break

    except:
        print(f'Error in row {i} done, song was number {j}')
        break


musicdata.to_csv('musicwithsongs.csv', sep=',')
songdata.to_csv('songsupdate.csv', sep=',')

print('DB uploaded to CSV successfully!')

