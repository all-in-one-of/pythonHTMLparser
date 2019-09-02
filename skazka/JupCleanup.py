
import re
import time
import unicodedata
import os
import bs4
from bs4 import BeautifulSoup
import csv
from support import selectionAct



class Line():
	'''gets line with characterId as int text itself as string ,physical action as list of integers,scene number,line number'''
	def __init__(self,charId,name,tex,act,idSc,lineNum,timing,tT):
		self.charId=charId
		self.name=name
		self.tex=tex
		self.act=act
		self.idSc=idSc
		self.lineNum=lineNum
		self.timing=timing
		self.tT=tT



class Char():
	def __init__(self,charId,name):
		self.charId=charId
		self.name=name
		#list of lines for this character (class Line)
		self.lines=[]
		
TPrev=2
tT=0
textFile=open("index.html")
text1=textFile.read()
soup1 = BeautifulSoup(text1,"html.parser")

for x in soup1.find_all():
    if len(x.get_text(strip=True)) <= 1:
        x.extract()
    
span=soup1.find_all("span")
actors=[]
actorsId=0
for spa in span:
	
	for key, value in spa.attrs.items():
		if "#ff0000" in value:
			
			actem=spa.text.strip(" ")
			actem=actem.strip("\n")
			actors.append(Char(actorsId,actem))
			actorsId=actorsId+1
			
			
#adding actor " description " for underlined text

descrId=len(actors)
actors.append(Char(descrId,"DESCRIPTION"))

for ite in actors:
	print(ite.name+" ID " +str(ite.charId))		

linesTotalSec=[]
lineNumberSec=0
idSc=[]
colResult=re.search('color:#(.*);font-weight',value).group(1)
for index,spa in enumerate(span):
    
    for key, value in spa.attrs.items():
        if "underline" in value:
            colResult=re.search('color:#(.*);font-weight',value).group(1)
            linesTotalSec.append( Line(descrId,"DESCRIPTION",spa.text,colResult,idSc,lineNumberSec,TPrev,tT))
            lineNumberSec=lineNumberSec+1
        elif "italic" in value:
        	for actind ,act in enumerate(actors):
        		if span[index-1].text.upper().startswith(act.name.upper()):
        			colResult=re.search('color:#(.*);font-weight',value).group(1)
        			
        			linesTotalSec.append( Line(actind,act.name,spa.text,colResult,idSc,lineNumberSec,TPrev,tT))
        			lineNumberSec=lineNumberSec+1

              

print("color")
for lineSec in linesTotalSec:
	print(lineSec.tex+"lineActor"+ actors[lineSec.charId].name)


r=""
index=0
while r !="q" and  (index+1)<len(linesTotalSec):
	begin = time.time()
	print ("proceed?")
	print(linesTotalSec[index].tex)
	r=input() 
	#this is when you start typing
	#this would be after you hit enter
	end = time.time()
	elapsed = end - begin
	linesTotalSec[index].timing=elapsed
	tT=tT+elapsed
	linesTotalSec[index].tT=tT
	print(elapsed)
	print(tT)
	print(str(len(linesTotalSec)))
	print(str(index)+"index")
	index=index+1
[print(item.tex+" "+str(item.timing)) for item in linesTotalSec]

#input for actions into idSc string
r=""
index=0
while r !="q" and  (index+1)<len(linesTotalSec):
	print(linesTotalSec[index].tex)
	print(linesTotalSec[index].idSc)
	print("who is listening 0-9")
	for ind,ac in enumerate(actors):
		print(ac.name+"->"+str(ac.charId)+"\n")
	actTo=input()
	print("item the actor has 0-9")
	print("to be implemented in text")
	item=input()
	print("move typeof the actor 0-9")
	print( "from idle to agressive")
	movType=input()

	#this is when you start typing
	linesTotalSec[index].idSc.append(actTo)
	linesTotalSec[index].idSc.append(item)
	linesTotalSec[index].idSc.append(movType)
	print(linesTotalSec[index].idSc)
	print ("proceed? or repeat ->r" )
	r=input()
	if r=="r":
		pass
	else:
		index=index+1
	

for items in linesTotalSec:
	for index,char in enumerate(actors):
		if items.charId==char.charId:
			#empty and refill the actors text list from linesTotal list 
			#then fill them with parameters or add parameters to the existing from text
			#char.lines.clear()
			char.lines.append(items)

for actor in actors:
	for item in actor.lines:
	
	#time.sleep(item.timing)
		print(item.tex +"  Actor "+ str(item.name)+" time " + str(item.timing)+"\n")

textFile.close()


with open("output.csv",'w') as outputFile:
	wr=csv.writer(outputFile,dialect='excel')
	for lin in linesTotalSec:
		oneLine=[]
		oneLine.append(lin.charId)
		oneLine.append(lin.name)
		oneLine.append(lin.tex)
		oneLine.append(lin.act)
		oneLine.append(lin.idSc)
		oneLine.append(lin.lineNum)
		oneLine.append(lin.timing)
		oneLine.append(lin.tT)
		print(oneLine)
		wr.writerow(oneLine)
with open("output.csv","r") as file_obj:	
	reader = csv.reader(file_obj, delimiter=',')
	myScriptList=list(reader)
	#will print first element in csv line list as string
	for line in myScriptList:
		print(line[0])
		