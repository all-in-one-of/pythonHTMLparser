# -*- coding: utf-8 -*-
import time
from  bs4 import BeautifulSoup
import re
import csv
import json




class Line():
	'''gets line with characterId as int text itself as string ,physical action as list of integers,scene number,line number'''
	def __init__(self,charId,name,tex,act,lineNum,timing,tT):
		self.charId=charId
		self.name=name
		self.tex=tex
		self.act=act
		self.idSc=[]
		self.lineNum=lineNum
		self.timing=timing
		self.tT=tT
		self.soundFile=""






class Char():
	def __init__(self,charId,name):
		self.charId=charId
		self.name=name
		#list of lines for this character (class Line)
		self.lines=[]

def objCreator(d):
	line=Line(d["charId"],d["name"],d["tex"],d["act"],d["lineNum"],d["timing"],d["tT"])
	line.soundFile=d["soundFile"]
	line.idSc=d['idSc']
	return line

#generates list of actors id from globla list linesTotalSec
def generateListActId(_linesTotalSec):
    listOfId=[]
    for item in _linesTotalSec:
        if item.charId not in listOfId:
            listOfId.append(item.charId)
    listOfId.sort()
    return listOfId


def readFileListOfLines (fileName,_linesTotalSec):
	#temp values to fill the class variables
	#reads html file. the underlined strings are descriptions of the story
	#the italic strings are the dialogs
	#reads the color value of the string and creates an RGB tuple
	# red text defines an actors list
	# if text is italic list of actors is compared to prev span beginning and
	#adds an actor id. all this is forming list of objects.  _linesTotalSec
	
	_TPrev=2
	_tT=0
	textFile=open(fileName, encoding="utf8")
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
	
	
	lineNumberSec=0
	
	colResult=re.search('color:#(.*);font-weight',value).group(1)
	for index,spa in enumerate(span):
	   # iterates through dictoionary of bs4 span values
	    for key, value in spa.attrs.items():
	        if "underline" in value:
	            colResult=re.search('color:#(.*);font-weight',value).group(1)
	            colRGB=tuple(int(colResult[i:i+2], 16) for i in (0, 2, 4))
	            tex=spa.text.replace("(","").replace(")","")
	            _linesTotalSec.append( Line(descrId,"DESCRIPTION",tex,colRGB,lineNumberSec,_TPrev,_tT))
	            lineNumberSec=lineNumberSec+1
	        elif "italic" in value:
	        	for actind ,act in enumerate(actors):
	        		if span[index-1].text.upper().startswith(act.name.upper()):
	        			colResult=re.search('color:#(.*);font-weight',value).group(1)
	        			colRGB=tuple(int(colResult[i:i+2], 16) for i in (0, 2, 4))
	        			
	        			
	        			_linesTotalSec.append( Line(actind,act.name,spa.text,colRGB,lineNumberSec,_TPrev,_tT))
	        			lineNumberSec=lineNumberSec+1
	textFile.close()    			
	return _linesTotalSec,actors
	

	
		
			
					
def selectionAct(_linesTotalSec,_actors):
		#input for actions into idSc string
		#that makes a list of descriptions for the dialog
		# may need to implement some conditions and submenues
		#currently is:id of listener,id of item speaker has,
		#movement loop id,distance to the listener
	r=""
	index=0
	while r !="q" and  (index+1)<len(_linesTotalSec):
		print(_linesTotalSec[index].tex)
		print(_linesTotalSec[index].idSc)
		print("who is listening 0-9")
		#lists all actors for selection menu
		for ind,ac in enumerate(_actors):
			print(ac.name+"->"+str(ac.charId)+"\n")
		actTo=input()
		print("item the actor has 0-9")
		print("to be implemented in text")
		item=input()
		print("move typeof the actor 0-9")
		print( "from idle to agressive")
		movType=input()
		#distance between actors
		print("distance between actor 0-9")
		distType=input()
	
		#this is when you start typing
		_linesTotalSec[index].idSc.clear()
		_linesTotalSec[index].idSc.append(int(actTo))
		_linesTotalSec[index].idSc.append(int(item))
		_linesTotalSec[index].idSc.append(int(movType))
		_linesTotalSec[index].idSc.append(int(distType))
		print(_linesTotalSec[index].tex)
		print(_linesTotalSec[index].idSc)
		print ("proceed? or repeat ->r" )
		r=input()
		if r=="r":
			index=index
		elif r!="r":
			index=index+1
	for id in _linesTotalSec:
		print (id.idSc)
	return _linesTotalSec




def timingLine( _linesTotalSec,_tT ):
	r=""
	index=0
	while r !="q" and  (index+1)<len(_linesTotalSec):
		begin = time.time()
		print ("proceed?")
		print(_linesTotalSec[index].tex)
		r=input() 
		#this is when you start typing
		#this would be after you hit enter
		end = time.time()
		elapsed = end - begin
		_linesTotalSec[index].timing=elapsed
		_tT=_tT+elapsed
		_linesTotalSec[index].tT=_tT
		print(elapsed)
		print(_tT)
		print(str(len(_linesTotalSec)))
		print(str(index)+"index")
		index=index+1
	return _linesTotalSec

def actorsListFill(_actors,_linesTotalSec):
	for items in _linesTotalSec:
		for index,char in enumerate(_actors):
			if items.charId==char.charId:
				#empty and refill the actors text list from linesTotal list 
				#then fill them with parameters or add parameters to the existing from text
				#char.lines.clear()
				char.lines.append(items)
	return _actors

# convert list of objects to dictionary
#and writes to JsonL file
def writeToJsonL(filename,listOfObj):
	with open(filename, 'w') as outfile:
		for i in range(0,len(listOfObj)):
			Ld={}
			item=listOfObj[i]
			Ld["charId"]=item.charId
			Ld["name"]=item.name
			Ld["tex"]=item.tex
			Ld["act"]=item.act
			Ld["idSc"]=item.idSc
			Ld["lineNum"]=item.lineNum
			Ld["timing"]=item.timing
			Ld["tT"]=item.tT
			Ld["soundFile"]=item.soundFile
			json.dump(Ld, outfile)
			outfile.write('\n')

def writeToCsvExt(fileCsvExt,_linesTotalSec):
	with open(fileCsvExt,'w') as outputFile:
		wr=csv.writer(outputFile,dialect='excel')
		for lin in _linesTotalSec:
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
		
if __name__ == "__main__":
    print ("executed as main")