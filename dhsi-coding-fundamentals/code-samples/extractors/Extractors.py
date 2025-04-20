# this program loads a PG file and extracts all geopolitical entities

# load all necessary modules
import re
import pprint
import nltk

#define a preprocessing function


#Open the file containing American Notes

notesText = open('AmericanNotes.txt')

#make legible to NLTK

t = notesText.read()
u = unicode(t, 'utf-8')

# perform preprocessing

sentences = nltk.sent_tokenize(u)
sentences = [nltk.word_tokenize(sent) for sent in sentences]
sentences = [nltk.pos_tag(sent) for sent in sentences]

outputList = []
for sent in sentences:
    s = nltk.ne_chunk(sent)
    s = str(s)
    sentGPE = re.findall('\(GPE.+?\)',s)
    print sentGPE
    for item in sentGPE:
        outputList.append(item)

outputFile = open("PlacesInAmericanNotes.txt","w")
for line in outputList:
    line = re.sub('\(GPE|\)|/NNP|/NNPS|/NN|/JJ',"",line)
    line = line.replace("StatesS","States")
    line = line.replace("NotesS","Notes")
    line = line.title()
    outputFile.write(line+"\n")
outputFile.close()

#Generate a list of place names to extract
#Boston, Lowell, Worcester, Hartford, New Haven, New York, Philadelphia, Washington, Richmond, Baltimore, Harrisburg, Pittsburg, Cincinnati, Louisville, St. Louis, Columbus, Sandusky, Laie Erie, Niagara Falls, Toronto, Kingston, Montreal, Quebec, St. John's, Lebanon, West Point
	
#Extract geographic place names





#Connect place names to geo-coordinates

#Map coordinates
