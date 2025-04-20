# Grab text files using shell
# Clean text files 
# Determine head and tail, then head -21749 moby.txt | tail -21729 > cleanestwhale.txt)

import re

# compile the regular expression for fast searches
sheTest = re.compile('(?:^|\W)([Ss]he(\s|\b)(?:.+?(?:\b|\s)){0,10})')
heTest = re.compile('(?:^|\W)([Hh]e(\s|\b)(?:.+?(?:\b|\s)){0,10})')
	
# Open and read file
with open('cleanpridenovel.txt', 'r') as f:
	pride_list = f.readlines()
# .readline makes a list of lines in text

finalList = []

for line in pride_list:
	wordList = line.split(' ')
	for word in wordList:
		finalList.append(word.strip())
		
finalList = ' '.join(finalList)

# Build Tokenizer		
# Find Instances of He and She (using iteration)
#pronounList = []
#for token in finalList:
	#if token == 'she':
		#pronounList.append(token)
	#elif token == 'he':
		#pronounList.append(token)
	#elif token == 'She':
		#pronounList.append(token)
	#elif token == 'He':
		#pronounList.append(token)
		#print(pronounList)
# Identify verb phrases following pronouns

sheSearchResults = sheTest.findall(finalList)
sheList = []

#Let's see the results
if sheSearchResults is not None:
    for she_results in sheSearchResults:
    # the [0] grabs the first item in the return value
    	sheList.append(she_results[0])
        
#print(sheList)

heSearchResults = heTest.findall(finalList)
heList = []

if heSearchResults is not None:
    for he_results in heSearchResults:
    # the [0] grabs the first item in the return value
    	heList.append(he_results[0])
        
with open ('she_pronouns.txt', 'w') as f:
	f.write(' '.join(sheList))
        
#print(heList)

# End JS help

# Visualize pronoun and modals based on levels of certainty 

# Repeat with subsequent texts and save as separate files

# Fancy comparative visualization

"""
Pride and Prejudice and Pronouns
This project compares pronoun and verb usage in Jane Austen's Pride and Prejudice and three film adaptations (the 1995 BBC production, the 2005 Joe Wright production, and the 2001 Bridget Jones's Diary adaptation), in an attempt to examine agency and degrees of certainty. We will capture the pronoun and the three words that follow directly.
"""