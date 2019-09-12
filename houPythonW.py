import json
import os
from support import selectionAct,timingLine,readFileListOfLines,writeToCsvExt,actorsListFill,objCreator,writeToJsonL
from support import generateListActId

import hou


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
                    
fbxPath="D:/HoudiniProj/HoudiniProjects/JsonProject/obj_fbx_tube.fbx"
node = hou.pwd()
geo = node.geometry()
workDir=os.getcwd()
data = []
print("DTJSon")
#reads json data using function from support into data list
with open("outputSdPath.jsonl") as f:
        for line in f:
                obj=(json.loads(line,object_hook=objCreator))
                print("DTJSon")
                print(obj)
                data.append(obj)
                
path="D:/downloads/pythonHTMLparser/skazka/sound/"
#generates list of actors id
idList=generateListActId(data)

geoRut=hou.node('/obj/geo1')

newChopObj=geoRut.createNode("chopnet")
globMerge=newChopObj.createNode("merge")

# imports fbx per actors id
fbxActList=[]
for idAct in idList:
# create object merge per imported fbx
#generate list of object merges
    fbNode=fbxMerge(fbxPath)
    fbxActList.append(fbNode)
    
for idAct in idList:
    idActList=[]
    fbxActList=[]
#create merge node an connect to it file with sound
#then rename channel and shifts it to time  per each    actId
    objMergeNode=newChopObj.createNode("merge")
    for dataId in data:
        if dataId.charId==idAct:
            idActList.append(dataId)
    connMerge=generate(idAct,objMergeNode,idActList,newChopObj)
    globMerge.setNextInput(connMerge)
            
                
hou.node('/obj/geo1/chopnet2').layoutChildren()
hou.node('/obj/geo1').layoutChildren()
#result list of obj merge nodes in geo 
# create cameras and scenes layout. scenes to be edited in interF? file
# distance between objects,orient
# distance doesent change within scenes
'''
myCam = hou.node(“/obj”).createNode(“cam”, “myCam”)
hou.hscript(“viewcamera -c ” + myCam.name() + “ *.*.world.persp1”)

script to iterate over different cameras

import hou, toolutils
 
cameraPathes = []
for n in hou.node('/').allSubChildren():
    if n.type().name().startswith("cam"):
        cameraPathes.append(n.path())
 
desktop = hou.ui.curDesktop()
scene_viewer = desktop.paneTabOfType(hou.paneTabType.SceneViewer)
viewport = scene_viewer.curViewport()
 
if viewport.camera()>0:
    index = cameraPathes.index( viewport.camera().path() )
    maximum = len(cameraPathes)
    index2 = (index+1)%maximum
    viewport.setCamera(hou.node(cameraPathes[index2]))
 
else:
    viewport.setCamera(hou.node(cameraPathes[0]))
    
    
anothe tut set up cam res

objNode = hou.node('/obj')
camNode = objNode.createNode('cam', ‘cameraName’)

camNode.parm(‘resx’).set(1920)
camNode.parm(‘resy’).set(1080)
'''