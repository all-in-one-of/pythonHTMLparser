print("&%-%%7484")
#import re
#import string
#import time
#from pygame import mixer
#mixer.init()

print("1111")

class Line():
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


print("fjfhfjfjfjjf")
f=open("krasnShap.txt",'r')
content=f.read()
f.close()
