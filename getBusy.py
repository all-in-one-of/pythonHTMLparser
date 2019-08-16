#Plays sound library .waits till the sound file ends 30 times per second #checks pygame.mixer.get_busy variable
import pygame
import sys


def printTest():
	print("GHJKKKJjJJJJ")
def playsound(soundfile):

    """Play sound through default mixer channel in blocking manner.
    
    This will load the whole sound into memory before playback
    """
    FR=30
    pygame.mixer.init()
    sound = pygame.mixer.Sound(soundfile)
    clock = pygame.time.Clock()
    sound.play()
    while pygame.mixer.get_busy():
        clock.tick(FR)
    pygame.QUIT

if __name__ == '__main__':
	sound='/storage/emulated/0/Download/Python/DatasetPy/audio.mp3'
	playsound(sound)
	
