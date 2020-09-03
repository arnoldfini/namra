import pandas as pd
import numpy as np
import re
import randomize

data = pd.read_csv(r'C:\Users\serio\OneDrive\Escritorio\music.csv', index_col=None, na_values=['NA'])

genre_db = data['artist.terms']

# Array where rock music index in the database will be stored
index = []

print("Starting...")

'''

Search for rock instances through the database. Store its index in index[]

'''

for key, genre in genre_db.iteritems():

    if re.search(r'rock', str(genre)):
        index.append(key)
        print(key+1, end=', ')

print()

'''

Create an array of numbers. Either 0 or 1. 
If the atribute selected is rock music for instance, only the index where there is a rock music song will have a value of 1.
Otherwise, 0.

'''

output = np.empty(len(data), dtype=int) # Create a 1 dimensional array

print(f"First i: ", end= "")

for i in range(len(index)):

    print(i, end=", ")

    temp = np.zeros(len(data)) # 1D array to store the only a '1' the index where the song belongs to. otherwise, 0

    temp[index[i]] = 1 # Set only the location of the rock song in data = 1

    output = np.add(output, temp) # Sum temp to output so only the indexes of rock music songs appear a 1

    np.round(output) # Round

print()

np.savetxt("output.csv", output, delimiter=',') # Save the output array as a csv file
print("Output csv successfully saved. ")


'''
output_arr = np.zeros([len(data), len(data)], dtype=int)

print(f"Second i: ", end= "")
for i in range(len(output)):

    print(i, end=", ")
    ran0 = random.randint(0, len(data))
    ran1 = random.randint(0, len(data))

    sumvect = np.add(output[ran0], output[ran1])
    np.round(sumvect)
    np.vstack([output_arr, sumvect])

print()

print(output_arr)

np.savetxt("output_vector.csv", output_arr, delimiter=',')

print("Copied output_arr into CSV successfully!")
'''
