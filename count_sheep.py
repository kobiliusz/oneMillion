from itertools import count
from time import sleep
import pyttsx3 as tts
from million import number_name

if __name__ == '__main__':
    tts_engine = tts.init()
    tts_engine.setProperty('rate', 150)
    tts_engine.setProperty('volume', 0.7)
    for no in count(1):
        try:
            words = number_name(no) + ' sheep'
        except NotImplementedError:
            exit(-1)
        print(words)
        tts_engine.say(words)
        tts_engine.runAndWait()
        sleep(.5)
