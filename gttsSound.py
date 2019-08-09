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

for itemT in data:
	tts = gTTS(text=itemT.tex, lang='en')
	tts.save("charId"+str(itemT.charId)+"lineNum"+str(itemT.lineNum)+".mp3")