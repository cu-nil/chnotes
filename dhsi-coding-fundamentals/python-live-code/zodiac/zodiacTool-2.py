#Here we start building the components, one by one, in the order that we need them.  Note that we are testing our ability to read the file by making sure that we can print it.  This won't be part of the actual program.  Note that we are also CLOSING the file (see the bottom).

#Open the zodiac file

zodiacText = open('zodiacDescriptions.txt')
for line in zodiacText:
    print line

#Load into a dictionary


#Ask user for input (year)


#Take year and use as a conditional (later we'll just access the dictionary directly)


#Return horoscope


#Repeat

zodiacText.close()

#Below is a description of the task

"""
While taking a class on the culture of China, you have learned about the Chinese zodiac in which people fall into 1 of 12 categories, depending on the year of their birth. The categories, numbered 0 to 11, correspond to the following animals: 
(0) monkey, (1) rooster, (2) dog, (3) pig, (4) rat, (5) ox, (6) tiger, (7) rabbit, (8) dragon, (9) snake, (10) horse, (11) goat. Those who believe in this zodiac think that the year of a person's birth influences both their personality and fortune in life.

To find your zodiac sign, divide the year of your birth by 12. The remainder then determines your sign. For example: The remainder when we divide 1985 by 12, is 5; therefore, a person born in 1985 is an ox according to the Chinese zodiac.
"""	