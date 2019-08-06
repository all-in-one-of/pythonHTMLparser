import pyttsx3
from gtts import gTTS
import gtts
import os
import pygame, time
from pygame import mixer
from tempfile import TemporaryFile
'''
engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("привет мир привет мир привет мир абракадабра ")
    engine.runAndWait()
    engine.stop()
'''
tts = gTTS(text="привет мир привет мир привет мир абракадабра ", lang='no')
tts.save("saved_file.mp3")
sf = TemporaryFile()
mixer.init()
tts.write_to_fp(sf)
sf.seek(0)
mixer.music.load(sf)
mixer.music.play()



pygame.init()
pygame.mixer.music.load('C:/TempProxy/UStudio/gitHub/pythonHTMLparser/saved_file.mp3')
pygame.mixer.music.play()
time.sleep(5)
print(gtts.lang.tts_langs())

