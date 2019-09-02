import re
import string

class Lines():
	'''gets line with characterId as int text itself as string ,physical action as list of integers,scene number,line number'''
	def __init__(self,charId,tex,act,sceneNum,lineNum):
		self.charId=charId
		self.tex=tex
		self.act=act
		self.sceneNum=sceneNum
		self.lineNum=lineNum
class Char():
	def __init__(self,charId,name):
		self.charId=charId
		self.name=name
		self.lines=[]

f=open("krasnShap.txt",'r')
content=f.read()
f.close()

head=re.findall(r'<head>(.*?)</head>',content,re.DOTALL)[0]
#names for actors in id order
listAct=[item for item in head.split("\n") if item]
print(listAct)
#parts of the play
parts=re.findall(r'<p>(.*?)</p>',content,re.DOTALL)

for idSc,line in enumerate(parts):
	textLine=re.findall(r'<h>(.*?)</h>',line)
	print (textLine)
	for idLin,cha in enumerate(textLine):
		persTex=cha.split("/e>")
		persEmo=[int(i) for i in re.findall(r'<e>(.*?)</e>',cha)[0].split(",")]
		print(persTex[1])
		print(persEmo)
	