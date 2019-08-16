#Plays sounds from JsonL file for testing

import json
import pygame
import time
import os
from getBusy import playsound

from support import selectionAct,timingLine,readFileListOfLines,writeToCsvExt,actorsListFill,objCreator,writeToJsonL

#data must be the same as linesTotalSec
data = []
print("DTJSon")
with open("outputSdPath.jsonl") as f:
	for line in f:
		obj=(json.loads(line,object_hook=objCreator))
		print("DTJSon")
		print(obj)
		data.append(obj)
		
for item in data:
		sound=item.soundFile
		playsound(sound)
		time.sleep(item.timing)
	
	
