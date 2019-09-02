import json
import os
from support import selectionAct,timingLine,readFileListOfLines,writeToCsvExt,actorsListFill,objCreator,writeToJsonL
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
net2=hou.node('/obj/geo1/chopnet2')
objMergeNode=net2.createNode("merge")
for index,item in enumerate(data):
                sound=item.soundFile.rsplit("/",1)[1]
                
                nodestocopyF=(net1.node("file2"),)
                newcopiesF=net2.copyItems(nodestocopyF)
                newcopiesF[0].setName(sound)
                newcopiesF[0].parm("file").set(path+sound)
                
                nodestocopyR=(net1.node("rename3"),)
                newcopiesR=net2.copyItems(nodestocopyR)
                newcopiesR[0].setName(str(index)+"rename")
                newcopiesR[0].setInput(0,newcopiesF[0])
                newcopiesR[0].parm("renameto").set("chan"+str(index))
                
                nodestocopyS=(net1.node("shift2"),)
                newcopiesS=net2.copyItems(nodestocopyS)
                newcopiesS[0].setName(str(index)+"shift")
                newcopiesS[0].setInput(0,newcopiesR[0])
                newcopiesS[0].parm("start").set(index)
                
                objMergeNode.setNextInput(newcopiesS[0])
                
hou.node('/obj/geo1/chopnet2').layoutChildren()

