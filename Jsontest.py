#todo TTS convert
#todo write jsonl file with addresses of sound files
#write sound files to diff directories
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

from support import selectionAct,timingLine,readFileListOfLines,writeToCsvExt,actorsListFill,objCreator,writeToJsonL

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
	filename="charId"+str(item.charId)+"lineNum"+str(item.lineNum)+".mp3"
	if item.charId>=0:
		sound='/storage/emulated/0/Download/skazka/'+filename
		playsound(sound)
		time.sleep(item.timing)
	
	
