#Purpose:  To take all the files from a desginated directory and use TextBlob
#	to print all sentiment analysis values to a .csv file
#
#Other TextBlob tools can be used by reconfiguring that part of this script


#Initialize TextBlob
from textblob import TextBlob as tb

#First task:  Read in files in directory as list
import os
Poems = os.path.dirname("Poems/")

#1.a: define filelist as list and filename as string
filelist =[]
filename =""

#1.b:  These commands walk the directory structure and create an accessible filelist
#	strings are the required input type for TextBlob

for root, dirs, files in os.walk(Poems):
	for file in files:
		filelist.append(os.path.join(root, file))
		
#1.c:  Read each file in using filepath to 

for filepath in filelist:
	
	# print each file as it is read in
	
	print(filepath)
	
	# open each file and read them into a long string
	collins = open(filepath, "r")
	CollinsPoem=[]
	for lines in collins:
		CollinsPoem.append(lines.strip())

	CollinsPoemString = " ".join(CollinsPoem)

# Second Task:  Call TextBlob

	CollinsBlob =tb(CollinsPoemString)
	print('Placeholdername', CollinsBlob.sentiment.polarity, CollinsBlob.sentiment.subjectivity)

	# set variables to string type
	p=""
	s=""
	printline=""

	#assign tb string values to variables
	p=str(CollinsBlob.sentiment.polarity)
	s=str(CollinsBlob.sentiment.subjectivity)

	#build string to write to file
	printline=filepath+","+p+","+s

	#write to file with linebreak
	f = open('workfile', "a")
	f.write(printline+"\n")

#close output file
f.close()
