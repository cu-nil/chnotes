# created directories
# created textfile from URL
# moved textfile to TextWrangler

# print("Hello World")
# Scope
# Goal/stage 1: To write a program that will pull an abstract from a page of the Branch Collective Website
# To add language that will associate the title of an article abstract in a list
# Goal/stage 2: To add a function to that program that will use a list of pre-given URLs to pull several abstracts from standard pages of the Branch Collective Website
# Goal/stage 3 (big goal): To add language to our program that will pull website map data from the Branch Collective about individual pages with abstract, and will convert this data into a list that will automatically grab abstract data from pages in that list
# Goal/stage 4: To add language to our program that would navigate to target website/crawl the web for similar websites.


# Goal/stage 1: 
# To write a program that will pull an abstract from a page of the Branch Collective Website
# To add language that will associate the title of an article abstract in a list
# Begin working with CURL and WGET
# Begin with the Culture section of the Branch collective & pull the abstract from the first article, by Thomas Mclean.
# For each item in this list look for the word "Abstract"

# Next Step:
# with open(path + 'Branch.txt", 'r') as b: "This is the first function to gain access to this text file; we created it by using a Shell Script curl to dump it into a text file.
# we then opened that text file and made it readable as variable (i.e. dumped it into a container as "b")
# we then created a variable that reads "b" as a list of strings (i.e. turned the text a list of strings using .readlines--method, which is a special function)
# each line is a string
# Branch_list is a way of reading variable "b" in this way; Branch_list is just a way to read "b" in a new way
# then we displayed it with the function print, displaying only line 84
# we determined the line by looking at the text; we identified the string in the list to grab; then we grabbed it by using the function, print
# we displayed that string using the variable established to isolate that string, we were able to do this because Branch_list makes the text readable as a list of strings

# Next Step:
# strip the html tags from the output

# Next Step:
# Save the clean file to a .csv file or .txt file

#with open('Branch.txt', 'r') as b:
    #Branch_list = b.readlines()

    # Branch_range = len(Branch_list) - 1
    # print(Branch_list[84])
    
#import re
#FinalString = (re.sub('<[^>]*>', '', Branch_list[84]))

    
#FinalString = (re.sub('<[^>]*>', '', Branch_list[84]))

# print(re.sub('<[^>]*>', '', Branch_list[84]))


#with open('WS_Output.txt', 'w') as c:
    #c.write(FinalString)

    #c.write('Hello World')
    
# print(type(Branch_list[84]))




    #return Branch_list[Branch_list[84]
    
    
    

# import re
# re.sub('<[^>]*>', '', Branch_list[84])


    
#import mechanize
#br = mechanize.Browser()
#br.open("http://http://www.branchcollective.org/?ps_topic=culture/")

 


     
#print(len(Branch_list))

# final_string = re.sub('<[^>]*.', '', web_list[84])
#final_string = re.sub('<[^>]*.', '', web_list[84])



#import re

#with open ('Branch.txt', 'r') as w:
     #Branch_list = w.readlines()
     #FinalString = (re.sub('<[^>]*>', '', Branch_list[84]))

#with open('testing.txt', 'w') as f:
    #f.write(FinalString)
    
# import urllib.request

#with urllib.request.urlopen('http://www.branchcollective.org/?ps_articles=erika-rappaport-object-lessons-and-colonial-histories-inventing-the-jubilee-of-indian-tea') as response:
 #   html = response.read()
 #   print(html)
    
#import urllib.request
#from bs4 import BeautifulSoup

#with urllib.request.urlopen('http://www.branchcollective.org/?ps_articles=erika-rappaport-object-lessons-and-colonial-histories-inventing-the-jubilee-of-indian-tea') as response:
 #   soup = BeautifulSoup(response.read(), 'html.parser')
    #print(soup.prettify())
  #  print(soup.find("div", class_="extract").get_text()) #we need a method called "get child" to get the second child 
    
# Good code from 102 to 108




import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen('http://www.branchcollective.org/?page_id=13') as response:
    soup = BeautifulSoup(response.read(), 'html.parser')
    
    #we first find all the list items with the class "cat-item"
    listItems = soup.find_all("li", class_="cat-item")
    
    #we then iterate over the responses to get the hrefs.
    topicURLs = []
    for item in listItems:
        #print(item.find('a').get('href')))
        topicURLs.append(item.find('a').get('href'))
    
    #print(topicURLs)
    
    #we take the topic URLs and for each we load the page and extract the main article pages it links to
    #by recognizing that each of these links is inside a div tag with the ps_articles class.
    categoryAbstracts = []
    for url in topicURLs:
        with urllib.request.urlopen(url) as response2:
            soup = BeautifulSoup(response2.read(), 'html.parser')
            divItems = soup.find_all("div", class_="ps_articles")
            #print(url, divItems)
            for div in divItems:
                categoryAbstracts.append(div.get_text().strip())
    #print(categoryAbstracts)

with open('ALL_ABSTRACTS.txt',"w") as f:
	for abstract in categoryAbstracts:
		f.write(abstract)
		f.write('\n\n\n')