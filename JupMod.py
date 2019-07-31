#pylint:disable=E0602

import re
import time
import unicodedata
import os
import bs4
from bs4 import BeautifulSoup
import csv
from support import selectionAct,timingLine,readFileListOfLines,writeToCsvExt,actorsListFill




		
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
[print(item.tex+" "+str(item.timing)) for item in linesTotalSec]

#input for actions into idSc string
linesTotalSec=selectionAct(linesTotalSec,actors)
print(linesTotalSec[1].idSc)

#fills actors lis with text lines
actors=actorsListFill(actors,linesTotalSec)

for actor in actors:
	for item in actor.lines:
		print(item.tex +"  Actor "+ str(item.name)+" time " + str(item.timing)+"\n")
		print(item.idSc)

#writes csv to disk linestotalSec
writeToCsvExt("output.csv",linesTotalSec)


		