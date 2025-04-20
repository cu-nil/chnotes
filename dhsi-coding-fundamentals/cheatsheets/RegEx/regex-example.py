#This is meant to be a short example of how to implement the re library in python
#a useful tool for learning and developing regular expressions is
# http://regexpal.com/

#regular expressions come for free but you have to ask for them
import re

#create a variable to hold the regular expression library
ourSearchExpression = re.compile('de.')
 
#check the type
print type(ourSearchExpression)

#check the content
print ourSearchExpression

#let's use the expression actually return the FIRST instance found
ourMatchAttempt = ourSearchExpression.search("abcdefghiklmnopqrstuvwxyzdex")
print ourMatchAttempt.group()

#let's use the expression actually return ALL instances
ourMatchAttempt = ourSearchExpression.findall("abcdefghiklmnopqrstuvwxyzdex")
print ourMatchAttempt