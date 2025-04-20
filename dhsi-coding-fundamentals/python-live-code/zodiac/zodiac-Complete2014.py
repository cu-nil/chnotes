# This is a program that will tell you your chinese zodiac sign
# It is equivalent to zodiacTool-8.py
# Perhaps more importantly, this is the end result of the version we built in class
# It will differ a bit from the step by step guides which were built in advance

#open stuff
def ZodiacSetup():
	zodiacText = open('zodiacDescriptions.txt','r')
	zodiacList = []
	for line in zodiacText:
		zodiacList.append(line)
	zodiacText.close()
	return zodiacList
	
def ZodiacFigure():
	try:
		birthYear = int(raw_input("What year were you born? "))
		listLocation = (birthYear - 4) % 12
		print "Your sign is",
		print zodiacList[listLocation]
	
	except ValueError:
		print "Sorry Dave, I'm afraid I can't make an int from that"
		birthYear = "Stop"
		
	return birthYear

zodiacList = ZodiacSetup()

birthYear = 0
while type(birthYear) is int:
	birthYear = ZodiacFigure()
	
"""
While taking a class on the culture of China, you have learned about the Chinese zodiac in which people fall into 1 of 12 categories, depending on the year of their birth. The categories, numbered 0 to 11, correspond to the following animals: 
(0) monkey, (1) rooster, (2) dog, (3) pig, (4) rat, (5) ox, (6) tiger, (7) rabbit, (8) dragon, (9) snake, (10) horse, (11) goat. Those who believe in this zodiac think that the year of a person's birth influences both their personality and fortune in life.

To find your zodiac sign, divide the year of your birth by 12. The remainder then determines your sign. For example: The remainder when we divide 1985 by 12, is 5; therefore, a person born in 1985 is an ox according to the Chinese zodiac.
"""