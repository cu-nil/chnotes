# this program takes an HTML file and extracts only the part containing the film script
# then strips out all HTML code and saves it as a .txt file

# import the beautifulsoup4 package (an html-reading package you can get by typin
# "pip install beautifulsoup4" in bash
import bs4

# and also import "os", which doesn't need to be downloaded
import os

# and also import "re," regular expressions, which doesn't need to be downloaded
import re

# set the path to import files from and to

inpath = 'dl/'
outpath = "texts/"

# create a list containing the names of all the files that need to be converted from 
# HTML to plain text.
directory = os.listdir(inpath)

# iterate through each file in the directory
for file in directory:

    # open the file and turn it into a Beautiful Soup object
	loadFile = open(inpath+file)
	soupFile = bs4.BeautifulSoup(loadFile)
	
	# pull out only the contents of the <pre> element (which contains the scripts)
	soupText = soupFile.select('pre')
	
	# turn the beautifulSoup text into a Python string 
	scriptText = str(soupText)
	
	#strip out all HTML tags in this string using regular expressions
	script = re.sub('<.+?>','',scriptText)
	
	#remove the .html from the end of the file name
	filename = file.split('.html')[0]
	
	#write the plain text script to a text file
	scriptFile = open(outpath+filename+'.txt','w')
	scriptFile.write(script)
	scriptFile.close()
	
	
    