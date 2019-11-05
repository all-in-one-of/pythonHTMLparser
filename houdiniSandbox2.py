import hou
import json
import random
import os
import sys
#adds path to locate modules
supPath="C:/test/pythonHTMLparser"
sys.path.append(supPath)
from supportNew import timingLine,readFileListOfLines,actorsListFill,objCreator,writeToJsonL,generateDictOfSceneAct,generateCamActPosition,genListActId

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
                

idList=genListActId(data)

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

