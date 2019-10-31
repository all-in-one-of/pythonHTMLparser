import hou

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
    
    
geoRut=hou.node('/obj/geo1')    
fbxPath=['C:/test/pythonHTMLparser/tom.fbx','C:/test/pythonHTMLparser/box.fbx',
'C:/test/pythonHTMLparser/pig.fbx','C:/test/pythonHTMLparser/toy.fbx',
'C:/test/pythonHTMLparser/tom.fbx','C:/test/pythonHTMLparser/box.fbx',
'C:/test/pythonHTMLparser/pig.fbx','C:/test/pythonHTMLparser/box.fbx']

obj,list=fbxMerge(fbxPath[2])
print(obj)
print("objPrinted")
print(list)
print("listPrinted")