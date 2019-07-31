import time
from  bs4 import BeautifulSoup
import re
import csv




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






class Char():
	def __init__(self,charId,name):
		self.charId=charId
		self.name=name
		#list of lines for this character (class Line)
		self.lines=[]






def readFileListOfLines (fileName,_linesTotalSec):
	#temp values to fill the class variables
	_TPrev=2
	_tT=0
	textFile=open(fileName)
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
	    
	    for key, value in spa.attrs.items():
	        if "underline" in value:
	            colResult=re.search('color:#(.*);font-weight',value).group(1)
	            _linesTotalSec.append( Line(descrId,"DESCRIPTION",spa.text,colResult,lineNumberSec,_TPrev,_tT))
	            lineNumberSec=lineNumberSec+1
	        elif "italic" in value:
	        	for actind ,act in enumerate(actors):
	        		if span[index-1].text.upper().startswith(act.name.upper()):
	        			colResult=re.search('color:#(.*);font-weight',value).group(1)
	        			
	        			_linesTotalSec.append( Line(actind,act.name,spa.text,colResult,lineNumberSec,_TPrev,_tT))
	        			lineNumberSec=lineNumberSec+1
	textFile.close()    			
	return _linesTotalSec,actors
	

	
		
			
					
def selectionAct(_linesTotalSec,_actors):
		#input for actions into idSc string
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
	
		#this is when you start typing
		_linesTotalSec[index].idSc.clear()
		_linesTotalSec[index].idSc.append(actTo)
		_linesTotalSec[index].idSc.append(item)
		_linesTotalSec[index].idSc.append(movType)
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
		#will print first element in csv line list as string
		for line in myScriptList:
			print(line[0])
if __name__ == "__main__":
    print ("executed as main")