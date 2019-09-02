#To do  import Jsonl into Houdini and create geo with animation and sound
import json
import io
import re
import time
import unicodedata
import os
import bs4
from bs4 import BeautifulSoup
import csv
from support import selectionAct,timingLine,readFileListOfLines,writeToCsvExt,actorsListFill,objCreator,writeToJsonL



EmoList=[":)",";)",":}",":|",":(",":[",":()",":[]",";>()",":>[]"]	

#reads formatted html page separate names, description is underlined
#text color is read into list
linesTotalSec=[]
linesTotalSec,actors=readFileListOfLines("index.html",linesTotalSec)

#prints resulted list
for lineSec in linesTotalSec:
	print(lineSec.tex+"lineActor"+ actors[lineSec.charId].name)

# set the timing for each line
tT=0
linesTotalSec=timingLine(linesTotalSec,tT)


#input for actions into idSc string
linesTotalSec=selectionAct(linesTotalSec,actors)
[print(item.tex+" "+str(item.timing)) for item in linesTotalSec]


#fills actors lis with text lines
actors=actorsListFill(actors,linesTotalSec)


writeToJsonL('output.jsonl',linesTotalSec)
writeToCsvExt("output.csv",linesTotalSec)


	
data = []
print("DTJSon")
with open('output.jsonl') as f:
	for line in f:
		obj=(json.loads(line,object_hook=objCreator))
		print("DTJSon")
		print(obj)
		data.append(obj)
print(data[5].tex)
print(data[1].idSc)
print(data[5].tT)

		