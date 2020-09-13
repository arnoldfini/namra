import pandas as pd

'''

To catch only the songs relevant to the model (the ones that are in the form)

'''

data = pd.read_csv(r'C:\Users\serio\PycharmProjects\namra\dataset-manipulation\songsyt_url.csv', encoding='ISO-8859-1')

form = pd.read_csv(r'C:\Users\serio\PycharmProjects\namra\Cuestionario de feedback musical (Responses).csv', encoding='ISO-8859-1')

songs = []

for k,v in form.iteritems():

   if k.endswith('1') or k.endswith('2'):
       continue

   else:
       songs.append(k)
       print(k)

print(songs)
print(len(songs))
