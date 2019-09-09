from gtts import gTTS
import os
import json
from support import selectionAct,timingLine,readFileListOfLines,writeToCsvExt,actorsListFill,objCreator,writeToJsonL

#generates sound files in /sound directory in current working dir
#reqiers good internet connection
#writes to Jsonl file ,each line is a Json string, adds sound file address
data = []
#path to sound files
pathStr=[]
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
	pathStr.append("%s.mp3" % os.path.join(directory,mp3name))
#assingning sound address strings to list of object
for i in range(len(data)):
	data[i].soundFile=pathStr[i]
	i+=1
	
#Todo not assigned path
writeToJsonL("outputSdPath.jsonl",data)
