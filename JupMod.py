#pylint:disable=E0602
# ToDo read csv file in a timing manner and print corresponding actions 
# add distance to the actions , why description and rasskazxhik is not 
#strings
import json
import io
import re
import time
import unicodedata
import os
import bs4
from bs4 import BeautifulSoup
import csv
from support import selectionAct,timingLine,readFileListOfLines,writeToCsvExt,actorsListFill,objCreator



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

# convert list of objects to dictionary
Lf={}
with open('output.jsonl', 'w') as outfile:
	for i in range(0,len(linesTotalSec)):
		Ld={}
		item=linesTotalSec[i]
		Ld["charId"]=item.charId
		Ld["name"]=item.name
		Ld["tex"]=item.tex
		Ld["act"]=item.act
		Ld["idSc"]=item.idSc
		Ld["lineNum"]=item.lineNum
		Ld["timing"]=item.timing
		Ld["tT"]=item.tT
		json.dump(Ld, outfile)
		outfile.write('\n')

writeToCsvExt("output.csv",linesTotalSec)


	
data = []
with open('output.jsonl') as f:
	obj=(json.load(f,object_hook=objCreator))
	data.append(obj)
	

'''
with open('data.json') as json_file:
    data = json.load(json_file)
    for p in data:
        print(p.idSc)
'''
		