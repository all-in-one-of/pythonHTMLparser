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
		self.idSc=[5,0,5,0,0]
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


#TODO list of items somehow

def writeToText(_linesTotalSec,fileN):
	#TODO condensed text of dialog an physical action after each
	#line. returns filepath

	interFile=open(fileN,'w')
	for element in _linesTotalSec:
		lineText=str(element.lineNum)+"\n"+str(element.charId)+" "+element.name+ " " + element.tex+"\n"
		lineDesc="DIST=5"+","+"ITEM=0"+","+"MOOD=5"+","+"TALK=0"+","+"SCEN=0"
		interFile.write(lineDesc+"\n"+lineText)
	interFile.close()

def textToTotalLines(_linesTotalSec,fileN):
	#TODO  get the filename from previous def 
	#and fills lineTotalSec with phy actions numbers
	fileR=open(fileN)
	index=0
	for line in fileR:
		if line.startswith("DIST="):
			values=line.strip().split(",")
			for number,item in enumerate(values):
				_linesTotalSec[index].idSc[number]=int(item[-1])
			index=index+1			
	return _linesTotalSec



def timingLine( _linesTotalSec,_tT ):
	r=""
	index=0
	totalTime=0
	#filling list with default timing values
	for timeFill in _linesTotalSec:
		#assuming 25 letters per second plus 1 sec pause
		timePerLine=len(timeFill.tex)/25+1
		totalTime=totalTime+timePerLine
		timeFill.timing=timePerLine
		timeFill.tT=totalTime

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
	with open(filename, 'w',encoding='utf8') as outfile:
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
			json.dump(Ld, outfile,ensure_ascii=False)
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


#replaced with writing to file and editing text		
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
	
	
#reads jsonl file into a list of objects
def readFromJsonL(filename,data ):	
	print("DTJSon")
	with open(filename) as f:
		for line in f:
			obj=(json.loads(line,object_hook=objCreator))
			
			data.append(obj)
	
	return data	
	
	

def readFileGenerateSceneInteger(filename,_testTotalSec=[]):
	"""
iterate through the list and generates integer with
numbers from left to right SceneNumber, charId involved
Keeps them in _testTotalSec list and writes to a file as well
	"""
	readFromJsonL(filename,_testTotalSec)
	totalSecCopy=_testTotalSec.copy()
	listOfScens=[]
	addStr=""
	for index,line in enumerate(_testTotalSec):
		addStr=""
		scNum=line.idSc[4]
		addStr=str(scNum)
		for ind,li in enumerate(totalSecCopy):
			if li.idSc[4]==scNum:
				addStr=addStr+str(li.charId)
		_testTotalSec[index].idSc[0]=addStr
	writeToJsonL(filename,_testTotalSec)
	return _testTotalSec
	
#todo linesTotalSec now contains information about scene and char in it
#it's in linesTotalSec[index].idSc[0] .First is the scene number and then in #the order of appearing char id.	
#need to iterate over list ,shift the camera and generate fbx import for #scenes
def generateDictOfSceneAct(filename,_linesTotalSec=[]):
	"""
	creates dictonary with keys SceneNumbers
	and values list of actors (list(set) with unic charId, list[0] is Scene number)
	"""
	readFromJsonL(filename,_linesTotalSec)
	currScene=1
	listOfActors=[]
	dictOfActors={}
	for index, line in enumerate(_linesTotalSec):
		scNumstr=(line.idSc[0])
		scNum=int(scNumstr[0])
		if scNum==currScene:
			
			listOfActors=[int(ch) for ch in scNumstr]
			listOfActors=list(set(listOfActors))
			listOfActors.insert(0,currScene)
			dictOfActors[currScene]=listOfActors
			currScene+=1
			print(listOfActors)
	return dictOfActors
	
def generateCamActPosition(_dictOfActors,offCamX=10,offActZ=2,offActX=1):	
	'''
	from dictonary with keys SceneNumbers
	and values list of actors (list(set) with unic charId, list[0] is Scene num
	creates list of camera position tulps per scene.
	creates dictionary with value as sceneNum and key s list of 
	tupls with [1:] containing character positions and [0] charId
	
	'''

	listOfCamTulps=[]
	dictOfActPos={}
	for key,value in _dictOfActors.items():
		#Scene number * by offset will give a camera position in X
		listOfCamTulps.append((value[0]*offCamX,0,0))
		print(listOfCamTulps)
	#iterate only portion of the list
	#adding Z offset plus and minus delta(letssay 3 in X)
		listPerScene=[]
		for index,ac in enumerate(value[1:]):
			
			if index%2==0:
				xOffset=value[0]*offCamX-offActX*(index-1)
			else:
				xOffset=value[0]*offCamX+offActX*(index-1)
			listPerScene.append((ac,xOffset,0,offActZ))
			
			
		dictOfActPos[value[0]]=listPerScene
		
	return listOfCamTulps,dictOfActPos

if __name__ == "__main__":
    print ("executed as main")