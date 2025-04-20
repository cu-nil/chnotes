#This program will tell a person their Chinese Zodiac animal when they provide their birth year.

def ZodiacSetup():

	#Open the file with the animal names
	zodiacText = open('zodiacDescriptions.txt')

	#Load the file into a list
	zodiacList = []
	for line in zodiacText:
		zodiacList.append(line.strip())
	
	#Because our parents taught us to close things we open
	zodiacText.close()
	
	#Because if we don't do this we'll lose it
	return zodiacList


def ZodiacInput():	
	try:
		#Ask user for input
		birthYear = int(raw_input('Enter your birth year whenever it\'s ok with you: '))

		#Take year and use it as a conditional
		listLocation = (birthYear - 4) % 12

		#Provide humane, readable output
		print "Congratulations!  You are",

		#adding a grammar checker
		vowels = ['a','e','i','o','u']

		#if the first letter of the animal is a vowel then...
		if zodiacList[listLocation][0].lower() in vowels:
			print "an",
		else:
			print "a",
	
		print zodiacList[listLocation]

	except ValueError:
		print "Please enter a year"
		birthYear = "Stop"
	
	return birthYear
	
#Repeat
zodiacList = ZodiacSetup()

birthYear = 0
while type(birthYear) is int:
	birthYear = ZodiacInput()

#The comment below is a description of the task

"""
While taking a class on the culture of China, you have learned about the Chinese zodiac in which people fall into 1 of 12 categories, depending on the year of their birth. The categories, numbered 0 to 11, correspond to the following animals: 
(0) monkey, (1) rooster, (2) dog, (3) pig, (4) rat, (5) ox, (6) tiger, (7) rabbit, (8) dragon, (9) snake, (10) horse, (11) goat. Those who believe in this zodiac think that the year of a person's birth influences both their personality and fortune in life.

To find your zodiac sign, divide the year of your birth by 12. The remainder then determines your sign. For example: The remainder when we divide 1985 by 12, is 5; therefore, a person born in 1985 is an ox according to the Chinese zodiac.
"""