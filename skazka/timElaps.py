import time
r=""
while r !="q":
	begin = time.time()
	print ("proceed?")
	r=input() #this is when you start typing
	#this would be after you hit enter
	end = time.time()
	elapsed = end - begin
	print (elapsed)