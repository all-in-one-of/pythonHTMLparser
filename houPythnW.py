import json
import os
from supportNew import timingLine,readFileListOfLines,actorsListFill,objCreator,writeToJsonL,generateDictOfSceneAct,generateCamActPosition,genListActId

import hou
geoRut=hou.node('/obj/geo1')
fbxPath="D:/HoudiniProj/HoudiniProjects/JsonProject/obj_fbx_tube.fbx"
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
    return objMergeNodeFBX

def generate(_actId,_objMergeNode,_data,_newChopObj):

    for index,item in enumerate(_data):
                    sound=item.soundFile.rsplit("/",1)[1]
                    
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
with open("outputSdPath.jsonl") as f:
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
    
    fbNode=fbxMerge(fbxPath)
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
            
                
hou.node('/obj/geo1/chopnet2').layoutChildren()
hou.node('/obj/geo1').layoutChildren()
