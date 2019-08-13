from gtts import gTTS
import os
import json
from support import selectionAct,timingLine,readFileListOfLines,writeToCsvExt,actorsListFill,objCreator


data = []
print("DTJSon")
with open('output.jsonl') as f:
	for line in f:
		obj=(json.loads(line,object_hook=objCreator))
		print("DTJSon")
		print(obj)
		data.append(obj)
workDir=os.getcwd()
directory=workDir+"/sound"
if not os.path.exists(directory):
    os.makedirs(directory)
for itemT in data:
	tts = gTTS(text=itemT.tex, lang='ru')
	mp3name="charId"+str(itemT.charId)+"lineNum"+str(itemT.lineNum)
	tts.save("%s.mp3" % os.path.join(directory,mp3name))