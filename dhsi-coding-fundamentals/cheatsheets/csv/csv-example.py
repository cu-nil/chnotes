#This is a short demonstration of how to use the csv library
import csv

#Create a variable to hold the open file.
#Note the additional input in the open function.  This 'r' opens the file read only.
fileVariable = open('food-example.csv', 'r')

#Create a variable that will hold the csv interpreter
csvVariable = csv.reader(fileVariable)

#See what's inside our
print csvVariable

#Open a file to hold our output
outputFile = open('food-output.csv','w')

#Create a variable to act as a csv writer
csvWriter = csv.writer(outputFile, delimiter=",")
#Move through the file and output the foods to a new file.
for line in csvVariable:
	print line[2]
	csvWriter.writerow([line[2],line[1]])

#Clean up
fileVariable.close()
outputFile.close()