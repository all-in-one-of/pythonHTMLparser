#TODO - write a readme so to understand pipeline
#TODO - write a module to merge interF.txt int JsonLine file
import json
import random
import os
import sys
#adds path to locate modules
sys.path.append("D:/downloads/pythonHTMLparser")
from support import selectionAct,timingLine,readFileListOfLines,writeToCsvExt,actorsListFill,objCreator,writeToJsonL
from support import generateListActId

import hou
geoRut=hou.node('/obj/geo1')
fbxPath="D:/downloads/pythonHTMLparser/pig.fbx"
def fbxMerge(_fbxPath):
    fbx=hou.hipFile.importFBX(_fbxPath)
    fbx[0].parm("scale").set(0.01)
    
    listFbx=fbx[0].children()
    for node in listFbx:
    
        print node.name()
        print fbx[0].name()
        
        pathObj="/obj/"+fbx[0].name()+"/"+listFbx[0].name()
        listFbx[0].parmTuple("t").set([0,2,0])
        
    objMergeNodeFBX=geoRut.createNode("object_merge") 
    objMergeNodeFBX.parm("objpath1").set(pathObj)
    objMergeNodeFBX.parm("xformtype").set(1)
    return objMergeNodeFBX,listFbx[0]

def generate(_actId,_objMergeNode,_data,_newChopObj):

    for index,item in enumerate(_data):
                    sound=item.soundFile.rsplit("/",1)[1]
                    
     def generate(_actId,_objMergeNode,_data,_newChopObj):

    for index,item in enumerate(_data):
                  newcopiesF=_newChopObj.createNode("file")
                    newcopiesF.setName(sound)
                    newcopiesF.parm("file").set(path+sound)
                    

                    newcopiesR=_newChopObj.createNode("rename")
                    newcopiesR.setName(str(_actId)+"_"+str(index)+"rename")
                    newcopiesR.setInput(0,newcopiesF)
                    newcopiesR.parm("renameto").set("chan"+str(index))
                    
                    newcopiesS=_newChopObj.createNode("shift")
                    newcopiesS.setName(str(_actId)+"_"+str(index)+"shift")
                    newcopiesS.setInput(0,newcopiesR)
                    newcopiesS.parm("start").set(item.tT)
                    
                    _objMergeNode.setNextInput(newcopiesS)
    return _objMergeNode               
                    

node = hou.pwd()
geo = node.geometry()
workDir=os.getcwd()
data = []
print("DTJSon")
with open("D:/downloads/pythonHTMLparser/outputSdPath.jsonl") as f:
        for line in f:
                obj=(json.loads(line,object_hook=objCreator))
                print("DTJSon")
                print(obj)
                data.append(obj)
                
path="D:/downloads/pythonHTMLparser/skazka/sound/"
net1=hou.node('/obj/geo1/chopnet1')

idList=generateListActId(data)
geoRut=hou.node('/obj/geo1')
newChopObj=geoRut.createNode("chopnet")

globMerge=newChopObj.createNode("merge")

fbxActList=[]
for idAct in idList:
    
    fbNode,objFbx=fbxMerge(fbxPath)
    trX=random.randint(1,5)
    objFbx.parmTuple('t').set([0,trX,0])
#test for creating and positioning cameras
    myCam = hou.node("/obj").createNode("cam","myCam")
    camTx=random.randint(1,1111)
    myCam.parmTuple('t').set([0,camTx,(camTx*0.3)])
    fbxActList.append(fbNode)
    
for idAct in idList:
    idActList=[]
    fbxActList=[]
    
    objMergeNode=newChopObj.createNode("merge")
    for dataId in data:
        if dataId.charId==idAct:
            idActList.append(dataId)
    connMerge=generate(idAct,objMergeNode,idActList,newChopObj)
    globMerge.setNextInput(connMerge)
            
                
hou.node('/obj/geo1/chopnet1').layoutChildren()
hou.node('/obj/geo1').layoutChildren()
