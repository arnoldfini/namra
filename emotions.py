import math

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


def angle(num):

    num = math.radians(num)
    polar = [math.cos(num), math.sin(num)]

    polar[0] = float('%.2f' % round(polar[0], 2))
    polar[1] = float('%.2f' % round(polar[1], 2))

    return tuple(polar)
