# Global annotation:
# This program extracts the abstract from the "Thomas McLean" entry on Branch Collective,
# gets rid of the HTML code in the abstract, and then dumps the clean text into a .txt file 
################
################

# Step 1: Read in the file
# We opened the text from our website into a .txt file using "curl" in shell
# We then opened that text file and made it readable as variable 'f'
# Using method .readlines We then created a variable that reads f as a list of strings
# .readlines makes each line readable as a string
# MyText is just a way to read 'f' as a list of strings, where the strings are lines

import re

with open('Thomas.txt', 'r') as f:
    MyText = f.readlines()
    

# Step 2: Grab the abstract from line 84, a string
# We identified the string in the list that we wanted to grab, which was the abstract
# Using the function print, we displayed that string
# To do so we used the MyText variable with print to isolate the string we wanted
# We were able to do this because MyText makes our file readable as a list of strings
    
    # old: print(MyText[84])

# Step 3: Strip the HTML tags from the output/clean it up
# We im

    
    FinalString = (re.sub('<[^>]*>', '', MyText[84]))
    
    #print(re.sub('<[^>]*>', '', MyText[84]))

# Step 4: Save the abstract to a .txt file

#with open('Thomas.txt', 'a') as b:

with open('WSOutput.txt', 'w') as b:
    b.write(FinalString)
    
    # print(type(FinalString))
    #b.write(str(MyText[84]))
    
    
    
    #b.write("hello world")
   
   
   
   
   # b.open('WSOutput.txt', 'w')




#with open ('WSOutput.txt', 'w') as a:
    # f.write(str( )
    
    
	#open('WSOutput.txt', 'w')

# Step 5: Go before step 1 and creata