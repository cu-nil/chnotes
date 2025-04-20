#Here we package everything up into functions and set a loop so we can run it again and again.  We also start using zodiacDescriptions2.txt so that descriptions of the signs are included.

#Open the zodiac file

def ZodiacSetup():
    zodiacText = open('zodiacDescriptions2.txt')
    #for line in zodiacText:
    #    print line

    #Load into a list
    zodiacList = []
    for line in zodiacText:
        zodiacList.append(line)

    zodiacText.close()

    return zodiacList

def ZodiacFigure():
    #Ask user for input (year)
    try:
        birthYear=int(raw_input('What year were you born: '))
        #Take year and use as a conditional (later we'll just access the dictionary directly)
        listIndex = (birthYear - 4) % 12
        print listIndex

        #Return character
        print "You are a ",
        print zodiacList[listIndex]

    except ValueError:
        print "You did not enter an integer"
        birthYear = "Stop"

    return birthYear

#Repeat
zodiacList = ZodiacSetup()

birthYear=0
while type(birthYear) is int:
    birthYear = ZodiacFigure()
    #print type(birthYear)

#Below is a description of the task

"""
While taking a class on the culture of China, you have learned about the Chinese zodiac in which people fall into 1 of 12 categories, depending on the year of their birth. The categories, numbered 0 to 11, correspond to the following animals:
(0) monkey, (1) rooster, (2) dog, (3) pig, (4) rat, (5) ox, (6) tiger, (7) rabbit, (8) dragon, (9) snake, (10) horse, (11) goat. Those who believe in this zodiac think that the year of a person's birth influences both their personality and fortune in life.

To find your zodiac sign, divide the year of your birth by 12. The remainder then determines your sign. For example: The remainder when we divide 1985 by 12, is 5; therefore, a person born in 1985 is an ox according to the Chinese zodiac.
"""
