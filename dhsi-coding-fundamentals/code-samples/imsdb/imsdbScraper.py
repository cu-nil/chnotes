# this script reads a provided CSV file containing the names, authors, and URLs of
# film scripts from an online database, downloads each of them and names the file
# according to the AuthorName_FilmTitle.html convention

# import all necessary modules: requests (external, for HTML requests), time, and csv
import requests
import time
import csv

# Create a string with the URL prefix used for each script
urlPre = "http://www.imsdb.com/scripts/"

# Define the output directory

outpath = "dl/"

# open the csv

with open('names_titles_machine.csv','rb') as f:
    reader=csv.reader(f)
    
    # iterate every row in the csv file, each of which contains a list with three elements:
    # 0=text name, 1= author name, 2= url
    
    for row in reader:
    
    #first, download the file from the url
        text = requests.get(urlPre+row[2])
        
        # include a try/except for 404 http errors.
        try:
            text.raise_for_status()
        except Exception as exc:
    	    print("The file %s didn't download correctly" % row[0])
    	
    	# next, make a nice variable with the name of the first author only (many scripts
    	# have multiple authors
    	firstAuthorName = row[1].split(',')
    	firstAuthorName = firstAuthorName[0].replace(" ","")
    	
    	# format the title by removing white space
    	titleName = row[0].replace(" ","")
    	
    	# now, start getting ready to write the file, following the naming convention
    	# AuthorName_TextName.txt 
        scriptText = open(outpath+firstAuthorName+"_"+titleName+".html", "wb")
        
        # Keep you up to date as the process proceeds
        print("You successfully downloaded %s!" % titleName)
        
        # Write the file to disc
        for chunk in text.iter_content(100000):
            scriptText.write(chunk)
        scriptText.close()
        
        # Wait 10 seconds before proceeding to the next text, so as not to alert the
        # server
        time.sleep(10)