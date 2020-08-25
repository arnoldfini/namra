'''

Psicology part of the input

Some questions will be asked, based on an actual psicology this will give us a clue about how is feeling the user.

'''

from inputweather import *
from emotions import *
import re

class Psicology:

    def __init__(self):

        self.emotion = self.feelbox()
        self.weather = self.weather()
        print(self.weather, self.emotion)

        #if self.weather > 30:


    def feelbox(self):

        # Let the user write whatever he wants and find easy patterns in the input that give an idea of whatever they are expecting to

        inp = input('How are you feeling right now? ')

        possibleInput = [key for key,value in emodict().items()]

        actualEmotion = [emotion for emotion in possibleInput if re.search(rf'{emotion}', inp)]

        # Mapping feeling into 2D plane coordinates

        emotiondict = emodict()

        feeling2d = (emotiondict[str(actualEmotion)])

        return feeling2d

    def weather(self):

        temp, location = getWeather()
        print(temp, location)

    def intensity(self):
        #if
        pass

    def positivity(self):
        pass

Psicology()



