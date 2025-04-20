# this project will provide a graphical map for a user who has cvs file with address information
# Import CSV file, open, read, extract just the address information
# columns c through f
# create of list of addresses
# find GPS coordinates for each address

# first must extract the relevant information from the cvs file.

import googlemaps
from datetime import datetime
import csv

# need to get a Google API key before doing this step
gmaps = googlemaps.Client(key='AIzaSyDd8XJPeiZoSjD44EKncR-awKHtCY1OMH4')

# create list of lists--so all addresses are in a single list
# add address lists to the list of lists
listoflists = []

with open ('Addresses 1.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        listoflists.append(row[2:6])
# print(listoflists)
# this function reads the cvs file and pulls out the rows c through f (1-6).
# we tried 2:5, but it left off zip codes in column f, so 2:5 captures, c, d, e, but not f
# this function pulls the specified columns, makes each address a list, then stuffs them into another list
		
		


for geo in listoflists:
    geocode_result = gmaps.geocode(" ".join(geo))
    # print(geocode_result)
lat = []
lng = []
# these coordinates appear in the form of a dictionary	

# Geocoding an address
for geo in listoflists:
    geocode_result = gmaps.geocode(geo)
#print(geocode_result)
    lat.append(geocode_result[0]['geometry']['viewport']['northeast']['lat']) 
    lng.append(geocode_result[0]['geometry']['viewport']['northeast']['lng']) 
    # print (lat,lng)
	
import gmplot
gmap = gmplot.GoogleMapPlotter(40.3, -75.6, 16)


#gmap.plot(lat, lng, 'cornflowerblue', edge_width=16)
#gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
#gmap.scatter(lat, lng, 'k' marker=True)
gmap.heatmap(lat, lng)
# never figured out how to get the scatter maps to work. What is k?

gmap.draw("mymap3.html")	

