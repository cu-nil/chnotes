# Grab text files using shell

# Clean text files 
# Determine head and tail, then head -21749 moby.txt | tail -21729 > cleanestwhale.txt)
	
# Open and read file
with open('cleanpridenovel.txt', 'r') as f:
	pride_list = f.readlines()

pride_string = " ".join(pride_list)

# .readline makes a list of lines in text

# Build Tokenizer

#finalList = []
#for line in pride_list:
	#wordList = line.split(' ')
	#for word in wordList:
		#finalList.append(word.strip())
		#print(word)
		
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

# Stuff from JS:
import nltk
# nltk.download()

#Load some text to work on.  Note the use of triple quotes to allow entering a string with line breaks as
#part of the actual code.  Of course, you'll be reading from a file
ourWords = """She. was angry and wanted her due.
She was wondering why the first line here wasn't being found in python but was in regex101.
Oh well, something to tweak later.
When he gave his promise to his father, he meditated within himself to increase the fortunes of his sisters by the present of a thousand
pounds a-piece.  He then really thought himself equal to it.  The
prospect of four thousand a-year, in addition to his present income,
besides the remaining half of his own mother's fortune, warmed his
heart, and made him feel capable of generosity.-- "Yes, he would give 
them three thousand pounds: it would be liberal and handsome! It would
be enough to make them completely easy.  Three thousand pounds! he
could spare so considerable a sum with little inconvenience."-- He
thought of it all day long, and for many days successively, and he did not repent at all ever.
He said 'She is awful.' She said 'He's a jerk.'"""

tokens = nltk.word_tokenize(pride_string)

text = nltk.Text(tokens)

text.concordance('she')
# End JS help

# Change to a list or sort by pronoun and modal use. 

# One group for he, one for she and then sort by modal.

# Visualize pronoun and modals based on levels of certainty 

# Repeat with subsequent texts and save as separate files

# Fancy comparative visualization

"""
Pride and Prejudice and Pronouns
This project compares pronoun and verb usage in Jane Austen's Pride and Prejudice and three film adaptations (the 1995 BBC production, the 2005 Joe Wright production, and the 2001 Bridget Jones's Diary adaptation), in an attempt to examine agency and degrees of certainty. We will capture the pronoun and the three words that follow directly.
"""