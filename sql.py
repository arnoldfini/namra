from emotions import *
import re

# spanish-english
emoinesp = emoreversetrans()
# english - 2D vector
emotovector = emodict()


def strto2d(v):

    twod = emotovector[v]

    return str(twod)

with open(r'C:\Users\serio\PycharmProjects\namra\musicpro - copia.txt', 'r', encoding= 'utf-8') as f:

        text = f.read()

        text = text.replace('Sí', '1') \
            .replace('No', '0')

        print(text)

        for key, value in emoinesp.items():
            print(key, value)
            text = text.replace(key, strto2d(value))

        #text = text.replace('(', '[').replace(')', ']')




with open("test1.txt", "w") as w:

    w.write(text)