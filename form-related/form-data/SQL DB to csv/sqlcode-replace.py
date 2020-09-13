from emotions import *

'''

Code to replace 'Yes', 'No' to 1, 0 respectively (etc) in a SQL query.

'''

# spanish-english
emoinesp = emoreversetrans()
# english - 2D vector
emotovector = emodict()


def strto2d(v):

    twod = emotovector[v]

    return str(twod)

with open(r'C:\Users\serio\PycharmProjects\namra\form-data\SQL DB to csv\sqlcode-answers-raw.txt', 'r', encoding= 'utf-8') as f:

        text = f.read()

        text = text.replace('Sí', '1') \
            .replace('No', '0')

        print(text)

        for key, value in emoinesp.items():
            print(key, value)
            text = text.replace(key, strto2d(value))



with open("sqlcode-answers-adapted", "w") as w:

    w.write(f'{text}')