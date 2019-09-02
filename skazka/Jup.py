#pylint:disable=E0001
import re
import time
import unicodedata
import os
import bs4
import lxml
from bs4 import BeautifulSoup



class Line():
	'''gets line with characterId as int text itself as string ,physical action as list of integers,scene number,line number'''
	def __init__(self,charId,tex,act,sceneNum,lineNum,timing):
		self.charId=charId
		self.tex=tex
		self.act=act
		self.sceneNum=sceneNum
		self.lineNum=lineNum
		self.timing=timing



class Char():
	def __init__(self,charId,name):
		self.charId=charId
		self.name=name
		#list of lines for this character (class Line)
		self.lines=[]
		

f=open("krasnShap.txt",'r')
content=f.read()
f.close()
head=re.findall(r'<head>(.*?)</head>',content,re.DOTALL)[0]
#names for actors in id order
listAct=[item for item in head.split("\n") if item]
#list of actors with the names
print(listAct)
#creates list of characer classes
charActors=[Char(index,name) for index,name in enumerate(listAct)]


# In[55]:


parts=re.findall(r'<p>(.*?)</p>',content,re.DOTALL)
body=re.findall(r'<body>(.*?)</body>',content,re.DOTALL)


# In[62]:
TPrev=2
lineNumber=0
linesTotal=[]
#list all lines
for idSc,line in enumerate(parts):
    textLine=re.findall(r'<h>(.*?)</h>',line)
    
    for idLin,cha in enumerate(textLine):

        persTex=cha.split("/e>")
        persEmo=[int(i) for i in re.findall(r'<e>(.*?)</e>',cha)[0].split(",")]
        
        lineNumber=lineNumber+1
      
  #calculate time of line and timing from beginning
        linesTotal.append(Line(persEmo[0],persTex[1],persEmo,idSc,lineNumber,TPrev))

r=""
index=0
while r !="q" and  (index+1)<len(linesTotal):
	begin = time.time()
	print ("proceed?")
	print(linesTotal[index].tex)
	r=input() 
	#this is when you start typing
	#this would be after you hit enter
	end = time.time()
	elapsed = end - begin
	linesTotal[index].timing=elapsed
	print(elapsed)
	print(str(len(linesTotal)))
	print(str(index)+"index")
	index=index+1
[print(item.tex+" "+str(item.timing)) for item in linesTotal]

for items in linesTotal:
	for index,char in enumerate(charActors):
		if items.charId==char.charId:
			#empty and refill the actors text list from linesTotal list 
			#then fill them with parameters or add parameters to the existing from text
			#char.lines.clear()
			char.lines.append(items)

for actor in charActors:
	for item in actor.lines:
	
	#time.sleep(item.timing)
		print(item.tex +"Actor "+ str(item.charId)+"time " + str(item.timing)+"\n")

'''textFile=open("index.html")
text=textFile.read()
soup = BeautifulSoup(text,"html.parser")

textFile.close()	


    
bTags = []
uTags=[]
aTags=[]

for i in soup.find_all('span', style=lambda x: x and 'italic' or 'underline' in x):

    bTags.append(i.text)
print(bTags)
for i in soup.find_all('span', style=lambda x: x and 'underline' in x):

    uTags.append(i.text)
print (uTags)
for i in soup.find_all('span', style=lambda x: x and '#ff0000' in x):

    aTags.append(i.text)
print (aTags)
'''
textFile=open("index.html")
text1=textFile.read()
soup1 = BeautifulSoup(text1,"html.parser")

for x in soup1.find_all():
    if len(x.get_text(strip=True)) <= 1:
        x.extract()
    
span=soup1.find_all("span")
actors=[]

for spa in span:
	print(spa.text+"<span text")
	for key, value in spa.attrs.items():
		if "#ff0000" in value:
			actem=spa.text.strip(" ")
			actem=actem.strip("\n")
			actors.append(actem)
#adding actor " description " for underlined text
actors.append("DESCRIPTION")
descrId=len(actors)-1
			
for index,spa in enumerate(span):
	spa.text.replace("\n"," ")
	for key, value in spa.attrs.items():
		if "italic" in value:
			print(spa.text+"+++italic")
			for act in actors:
				if span[index-1].text.startswith(act):
					print(act +"&&&&&&&")
linesTotalSec=[]
lineNumberSec=0
idSc=1
colResult=re.search('color:#(.*);font-weight',value).group(1)
for index,spa in enumerate(span):
    print (spa.text)
    for key, value in spa.attrs.items():
        if "underline" in value:
            print (spa.text+str(index))
            colResult=re.search('color:#(.*);font-weight',value).group(1)
            linesTotalSec.append( Line(descrId,spa.text,colResult,idSc,lineNumberSec,TPrev))
            lineNumberSec=lineNumberSec+1
        elif "italic" in value:
        	for actind ,act in enumerate(actors):
        		if span[index-1].text.startswith(act):
        			print(value)
        			colResult=re.search('color:#(.*);font-weight',value).group(1)
        			print( "span attr value"  + "#"+colResult)
        			lineNumberSec=lineNumberSec+1
        			linesTotalSec.append( Line(actind,spa.text,colResult,idSc,lineNumberSec,TPrev))
        elif "#ff0000" in value:
        	print (spa.text+str(index))
        	
        

print("color")
for lineSec in linesTotalSec:
	print(lineSec.tex+"lineActor"+ actors[lineSec.charId])
textFile.close()	