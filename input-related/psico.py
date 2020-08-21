'''

Psicology part of my input

Some questions will be asked, based on an actual psicology this will give us a clue about how is feeling the user.

'''

from inputweather import *
from emotions import *
import re

class Psicology:

    def __init__(self):

        self.emotion = feelbox()
        self.weather = weather()

    def feelbox(self):

        '''

        Let the user write whatever he wants and find easy patterns in the input that give an idea of whatever
        they are expecting to

        '''

        input = input('How are you feeling right now? ')

        possibleInput = [key for key,value in emodict()]

        actualEmotion = [emotion for emotion in possibleInput if re.search(rf'{emotion}', input)]

        return actualEmotion

    def weather(self):

        getWeather()
