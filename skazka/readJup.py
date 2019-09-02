#!/usr/bin/env python
# coding: utf-8

# In[37]:


import re
import string
#import time
#from pygame import mixer
#mixer.init()

print("¹111111")

# In[51]:


class Line():
	'''gets line with characterId as int text itself as string ,physical action as list of integers,scene number,line number'''
	def __init__(self,charId,tex,act,sceneNum,lineNum):
		self.charId=charId
		self.tex=tex
		self.act=act
		self.sceneNum=sceneNum
		self.lineNum=lineNum


# In[52]:


class Char():
	def __init__(self,charId,name):
		self.charId=charId
		self.name=name
		self.lines=[]


# In[53]:

print("fjfhfjfjfjjf")
f=open("krasnShap.txt",'r')
content=f.read()
f.close()


# In[54]:


head=re.findall(r'<head>(.*?)</head>',content,re.DOTALL)[0]
#names for actors in id order
listAct=[item for item in head.split("\n") if item]
print(listAct)
#creates list of characer classes
charActors=[Char(index,name) for index,name in enumerate(listAct)]


# In[55]:


parts=re.findall(r'<p>(.*?)</p>',content,re.DOTALL)
body=re.findall(r'<body>(.*?)</body>',content,re.DOTALL)


# In[62]:


lineNumber=0
linesTotal=[]
for idSc,line in enumerate(parts):
    textLine=re.findall(r'<h>(.*?)</h>',line)
    
    for idLin,cha in enumerate(textLine):
#curren line text as string
        persTex=cha.split("/e>")
        persEmo=[int(i) for i in re.findall(r'<e>(.*?)</e>',cha)[0].split(",")]
        print(persTex[1])
        print(persEmo)
        lineNumber=lineNumber+1
        print (str(lineNumber))
        linesTotal.append(Line(persEmo[0],persTex[1],persEmo,idSc,lineNumber))
#appends lines to the character class
        if persEmo[0]==0:
            charActors[0].lines.append(Line(persEmo[0],persTex[1],persEmo,idSc,lineNumber))
        elif persEmo[0]==1:
            charActors[1].lines.append(Line(persEmo[0],persTex[1],persEmo,idSc,lineNumber))
        elif persEmo[0]==2:
            charActors[2].lines.append(Line(persEmo[0],persTex[1],persEmo,idSc,lineNumber))
        elif persEmo[0]==3:
            charActors[3].lines.append(Line(persEmo[0],persTex[1],persEmo,idSc,lineNumber))
        elif persEmo[0]==4:
            charActors[4].lines.append(Line(persEmo[0],persTex[1],persEmo,idSc,lineNumber))
        elif persEmo[0]==5:
            charActors[5].lines.append(Line(persEmo[0],persTex[1],persEmo,idSc,lineNumber))   



print([item.tex for item in linesTotal])
#mixer.music.load('/storage/emulated/0/Download/Python/DatasetPy/audio.mp3')

#for item in charActors[1].lines:
'''
	mixer.music.play()
	if not mixer.get_busy():
	
		time.sleep(2)
		print(item.tex +"\n")'''



