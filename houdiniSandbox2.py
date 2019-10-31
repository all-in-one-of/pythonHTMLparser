import hou
import json
import random
import os
import sys
#adds path to locate modules
supPath="C:/test/pythonHTMLparser"
sys.path.append(supPath)
from support import selectionAct,timingLine,readFileListOfLines,writeToCsvExt,actorsListFill,objCreator,writeToJsonL
from support import generateListActId

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

def delSearch(patt):    
    results = []
    for n in hou.node('/obj/').children():
        if n.name().startswith(patt):
            print (n.path())
            results.append(n.path())
     
    print (len(results))            
    if len(results):
        for node_name in results:
            hou.node(node_name).destroy()
            
#reads jsonl file into a list of objects
def readFromJsonL(filename,data ):      
        print("DTJSon")
        with open(filename) as f:
                for line in f:
                        obj=(json.loads(line,object_hook=objCreator))
                        
                        data.append(obj)
        
        return data     
def fbxMerge(_fbxPath):
    fbx=hou.hipFile.importFBX(_fbxPath)
    fbx[0].parm("scale").set(0.01)
    #removes subnet object
    listFbx=fbx[0].extractAndDelete()
    for node in listFbx:
    
        print node.name()
        pathObj="/obj/"+listFbx[0].name()
        
    objMergeNodeFBX=geoRut.createNode("object_merge") 
    objMergeNodeFBX.parm("objpath1").set(pathObj)
    objMergeNodeFBX.parm("xformtype").set(1)
    return objMergeNodeFBX,listFbx[0]
    
def generateCamActPosition(_dictOfActors,offCamX=10,offActZ=-20,offActX=1):       
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

        
'''           
delSearch("materials")
n=hou.selectedNodes()
print(n)
k=n[0].extractAndDelete()
print(k)
'''
geoRut=hou.node('/obj/geo1')
fbxPath=['C:/test/pythonHTMLparser/tom.fbx','C:/test/pythonHTMLparser/box.fbx',
'C:/test/pythonHTMLparser/pig.fbx','C:/test/pythonHTMLparser/toy.fbx',
'C:/test/pythonHTMLparser/tom.fbx','C:/test/pythonHTMLparser/box.fbx',
'C:/test/pythonHTMLparser/pig.fbx','C:/test/pythonHTMLparser/box.fbx']
data = []

with open(supPath+"\output.jsonl") as f:
        for line in f:
                obj=(json.loads(line,object_hook=objCreator))
                print("DTJSon")
                print(obj)
                data.append(obj)
                

idList=generateListActId(data)

print(idList)

testDict=generateDictOfSceneAct(supPath+"\output.jsonl")
testCamTul,testDict=generateCamActPosition(testDict)

print('testCamTul')
print(testCamTul)
print('testDict')
print(testDict)
for camP in testCamTul:
    myCam = hou.node("/obj").createNode("cam","myCam")
    camTx=random.randint(1,1111)
    myCam.parmTuple('t').set(camP)
    
for key,value in testDict.items():
    #print("act in Scene")
    #for ActT in value[0][1:])
    for actor in value:
        print("Actor id")
        print(actor[0])
        fbNode,objFbx=fbxMerge(fbxPath[actor[0]])
        #objFbx.extractAndDelete()
        l=actor[1:]
        actTuple=tuple(l)
        objFbx.parmTuple('t').set(actTuple)
        print("actorPos")
        print(actTuple)

