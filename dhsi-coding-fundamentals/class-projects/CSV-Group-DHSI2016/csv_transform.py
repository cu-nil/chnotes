# This program will read iteratively over rows in a .csv file outputting a reformatted 
# .csv that indicates relationship links between agents in shared rows. It takes a structured
# table and builds an edge list on the basis of shared row.


# import the csv library
import csv

readCells = [7,9,10,11,12,13,14,15,17,19,21,     # Use this container called 'readCells' as a map for reading 'converted'
22,23,24,25,26,27,30,33,36,39,42,45,48,51,      # --it tells you the cells I care about
54,57,60,63,66,69,72,75,78,81]


with open("original_csv.csv", "r") as f:  # open and read the original csv file and assign it to a variable that we can do things to.
    converted = csv.reader(f)             # with a given csv, open and assign it to the variable f
    next(converted)
    #print(type(converted))               # read f in the csv.reader way of reading, and call that read object 'converted'
    #print(converted)                                

    for book in converted:
        book = next(converted)                 # for each row in item 'converted'...
        #print(type(book))
        print(book)
        pairsdictionary = { }
        booktitle = book[5]                     # the book is always in 6th position
        source = 0                      # the source begins at 6 (but how do we make this slowly move up?
        target = 1                     # the target begins at 8 (but how do we make this slowly move up?
        readCellLen = len(readCells)                          # the total length of each row-list is 35
        
        while source < len(readCells) -2:                    # while the source node we are on is less than the total length of the list - 2
            if book[readCells[source]] != '':       # and if the source value is not empty
                while target < len(readCells) -1:              # while the target value is less than the total length of the list - 1
                    if book[readCells[target]] != '':                              # and if the target value is not empty
                        print("source: ", book[readCells[source]], "target: ", book[readCells[target]], "book: ", booktitle)  # print the source and the target and the book
                    target += 1
            source += 1
            target = source + 1
            