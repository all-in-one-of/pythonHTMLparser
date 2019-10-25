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
	
testDict=generateDictOfSceneAct('output.jsonl')
testCamTul,testDict=generateCamActPosition(testDict)

print('testCamTul')
print(testCamTul)
print('testDict')
print(testDict)

		