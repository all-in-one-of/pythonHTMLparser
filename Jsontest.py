#todo TTS convert
import json
import io
import pygame
import re
import time
import unicodedata
import os
import bs4
from bs4 import BeautifulSoup
import csv
from getBusy import playsound

from support import selectionAct,timingLine,readFileListOfLines,writeToCsvExt,actorsListFill,objCreator

#data must be the same as linesTotalSec
data = []
print("DTJSon")
with open('output.jsonl') as f:
	for line in f:
		obj=(json.loads(line,object_hook=objCreator))
		print("DTJSon")
		print(obj)
		data.append(obj)
		
for item in data:
	if item.charId==0:
		sound='/storage/emulated/0/Download/Python/DatasetPy/audio.mp3'
		playsound(sound)
		time.sleep(item.timing)
	elif item.charId==1:
		sound="/storage/emulated/0/Download/skazka/good.mp3"
		playsound(sound)
		time.sleep(item.timing)
		
	
