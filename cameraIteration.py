
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