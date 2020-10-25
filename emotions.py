import math
import numpy as np

'''

Emotions that had been taken into account. They are classified into a 2D plane.

+ Info: https://aip.scitation.org/doi/pdf/10.1063/1.5039095

'''


def emodict():
    emotions = {

        # PART 1

        'Happy': angle(5),
        'Delighted': angle(20),

        'Excited': angle(48),
        'Astonished': angle(75),
        'Aroused': angle(80),

        # PART 2

        'Tense': angle(92),
        'Alarmed': angle(100),
        'Angry': angle(105),
        'Afraid': angle(120),
        'Annoyed': angle(134),

        'Distressed': angle(140),
        'Frustrated': angle(145),

        # PART 3

        'Miserable': angle(185),
        'Sad': angle(190),
        'Gloomy': angle(213),
        'Depressed': angle(215),

        'Bored': angle(235),
        'Droopy': angle(250),
        'Tired': angle(265),

        # PART 4

        'Sleepy': angle(275),
        'Calm': angle(310),

        'Relaxed': angle(315),
        'Satisfied': angle(317),
        'At ease': angle(320),
        'Content': angle(325),
        'Serene': angle(330),
        'Glad': angle(348),
        'Pleased': angle(355)
    }

    return emotions


def emoreverse():
    emotions = emodict()

    reverse = {v: k for k, v in emotions.items()}

    return reverse


def emodictrans():
    emociones = {

        # PART 1

        'Happy': 'Feliz',
        'Delighted': 'Encantado',

        'Excited': 'Emocionado',
        'Astonished': 'Asombrado',
        'Aroused': 'Excitado',

        # PART 2

        'Tense': 'Tenso',
        'Alarmed': 'Alarmado',
        'Angry': 'Enfadado',
        'Afraid': 'Asustado',
        'Annoyed': 'Irritado',

        'Distressed': 'Angustiado',
        'Frustrated': 'Frustrado',

        # PART 3

        'Miserable': 'Miserable',
        'Sad': 'Triste',
        'Gloomy': 'Melancólico',
        'Depressed': 'Deprimido',

        'Bored': 'Aburrido',
        'Droopy': 'Marchito',
        'Tired': 'Cansado',

        # PART 4

        'Sleepy': 'Adormecido',
        'Calm': 'Calmado',

        'Relaxed': 'Relajado',
        'Satisfied': 'Satisfecho',
        'At ease': 'A gusto',
        'Content': 'Contento',
        'Serene': 'Sereno',
        'Glad': 'Alegre',
        'Pleased': 'Muy satisfecho'
    }

    return emociones


def emoreversetrans():
    dict = emodictrans()

    reverso = {v: k for k, v in dict.items()}

    return reverso


def emocat():
    emotions = {

        # PART 1

        'Feliç': angle(5),
        'Encantat': angle(20),

        'Emocionat': angle(48),
        'Sorprès': angle(75),
        'Excitat': angle(80),

        # PART 2

        'Tens': angle(92),
        'Alarmat': angle(100),
        'Furiós': angle(105),
        'Espantat': angle(120),
        'Irritat': angle(134),

        'Angoixat': angle(140),
        'Frustrat': angle(145),

        # PART 3

        'Miserable': angle(185),
        'Trist': angle(190),
        'Melanconiós': angle(213),
        'Deprimit': angle(215),

        'Avorrit': angle(235),
        'Marcit': angle(250),
        'Cansat': angle(265),

        # PART 4

        'Adormit': angle(275),
        'Calmat': angle(310),

        'Relaxat': angle(315),
        'Satisfet': angle(317),
        'A gust': angle(320),
        'Content': angle(325),
        'Serè': angle(330),
        'Alegre': angle(348),
        'Molt satisfet': angle(355)
    }

    return emotions


def emocat_reverse():
    return {value: key for key, value in emocat().items()}


def angle(num):
    num = math.radians(num)
    polar = [math.cos(num), math.sin(num)]

    polar[0] = float('%.2f' % round(polar[0], 2))
    polar[1] = float('%.2f' % round(polar[1], 2))

    return tuple(polar)

'''
for key, value in emodict().items():

    if key == 'Happy':
        print('\nPART 1')

    elif key == 'Tense':
        print('\nPART 2')

    elif key == 'Miserable':
        print('\nPART 3')

    elif key == 'Sleepy':
        print('\nPART 4')


    print(key, value)
'''