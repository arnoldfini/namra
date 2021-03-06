from recommendations_algorithm.input_related.inputweather import get_weather
from emotions import *
import re
from time import sleep
import ast
import datetime
import requests
import recommendations_algorithm.input_related.cs50 as cs50

'''

Psychology part of the input

Some questions will be asked, based on an actual psychology this will give us a clue about how is feeling the user.

'''

emotion_dict = emocat()
emotion_list = [key for key, value in emotion_dict.items()]

# using now() to get current time
current_time = datetime.datetime.now()


class Psychology:

    def __init__(self):
        self.emotion = self.feelbox()

        if self.emotion is None:
            self.emotion = self.select_feelings()

        self.weather = self.weather()
        self.time = self.time()

    def feelbox(self):
        try:
            # Let the user write whatever he wants and find easy patterns in the input that give an idea of whatever
            # they are expecting to

            inp = cs50.get_string('Com et sents ara mateix? ')
            possibleInput = [key for key, value in emotion_dict.items()]

            try:
                actualEmotion = [emotion for emotion in possibleInput if re.search(rf'{emotion}', inp)][0]

            except IndexError:
                try:
                    actualEmotion = [emotion for emotion in possibleInput if re.search(rf'{emotion.lower()}', inp)][0]

                except IndexError:
                    return None

            # Mapping feeling into 2D plane coordinates
            feeling2d = (emotion_dict[str(actualEmotion)])

            return feeling2d

        except KeyError:
            return None

    def select_feelings(self):
        print("\nLlista d'emocions: ")
        sleep(1)

        i = 0
        for key, value in emotion_dict.items():
            print(f'{i}: {key}')
            i += 1

        input_emotions = cs50.get_int("\nNo hem entès el que volies dir.\nSelecciona UNA amb la que més t'identifiques "
                                      "ara mateix (el número).\nInput: ")
        input_index = ast.literal_eval(str(f'({input_emotions})'))

        emotion = emotion_dict[emotion_list[input_index]]

        # TO-DO: AVERAGE WITH MORE THAN ONE FEELING
        return emotion

    def time(self):
        return current_time.hour

    def weather(self):
        try:
            temp, location = get_weather()
            return temp

        except AttributeError:
            self.weather()

        except requests.exceptions.ConnectionError:
            print('-' * 50)
            prompt = cs50.get_string('\nError. Reconnecta a internet (escriu "r") o abandona el programa (escriu '
                                     'qualsevol altra tecla)')

            if prompt == 'r':
                pass

            else:
                print('\nPrograma abortat amb èxit.')
                exit()

            sleep(3)
            self.weather()

    def intensity(self):
        pass

    def positivity(self):
        pass





