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
from support import selectionAct,timingLine,readFileListOfLines,writeToCsvExt,actorsListFill,objCreator,writeToJsonL,writeToText,textToTotalLines

#reads jsonl file into a list of objects
def readFromJsonL(filename,data ):	
	print("DTJSon")
	with open(filename) as f:
		for line in f:
			obj=(json.loads(line,object_hook=objCreator))
			
			data.append(obj)
	
	return data	

#reads formatted html page separate names, description is underlined
#text color is read into list
linesTotalSec=[]
linesTotalSec,actors=readFileListOfLines("index.html",linesTotalSec)





#prints resulted list
for lineSec in linesTotalSec:
	print(lineSec.tex+"lineActor"+ actors[lineSec.charId].name)


print("read the existing output.jsonl(1) or generate new(2)")
deside=input()
if deside==str(2):
	tT=0
	# set the timing for each line from number of char
	linesTotalSec=timingLine(linesTotalSec,tT)
	writeToJsonL('output.jsonl',linesTotalSec)
	
	print("Merge with interF(press1) or Generate new interF(press2) file")
	deside=input( )
	if deside==str(2):
		writeToText(linesTotalSec,"interF.txt")
#writes intermediate file for scene number and mood,item editing
#reads interm file and writes to list 
	else:
		linesTotalSec=[]
		readFromJsonL("output.jsonl",linesTotalSec)
		textToTotalLines(linesTotalSec,"interF.txt")
		writeToJsonL('output.jsonl',linesTotalSec)
		print("merged output&interF")
else:
	linesTotalSec=[]
	readFromJsonL("output.jsonl",linesTotalSec)
	
	print("Merge with interF(press1) or Generate new interF(press2) file")
	deside=input( )
	if deside==str(2):
		writeToText(linesTotalSec,"interF.txt")
#writes intermediate file for scene number and mood,item editing
#reads interm file and writes to list 
	else:
		linesTotalSec=textToTotalLines(linesTotalSec,"interF.txt")
		writeToJsonL('output.jsonl',linesTotalSec)
		print("merged output&interF")
		
#TODO
# proc generates offsets in x axis corresponding to sceneId
# generates  characters in the scene(fbx, position with offset)
# generates cameras ( with offsets )
# ??? generate all in 0 0 0, then apply offsets




#small check if recorded jsonl and current list have equal numbers
testTotalSec=[]
readFromJsonL("output.jsonl",testTotalSec)
for i in testTotalSec:
	print (i)
for index,el in enumerate(linesTotalSec):
	if (el.tT==testTotalSec[index].tT):
		print("True")
	else:
		print("False")

