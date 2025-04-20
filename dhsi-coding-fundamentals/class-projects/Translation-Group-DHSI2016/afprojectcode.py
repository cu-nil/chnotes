import time

#1.  read in two poems from a file
orgrussian = open("afrussian.txt")
contentorgrussian = orgrussian.read()
#print(contentorgrussian)

orgenglish = open("afenglish.txt")
contentorgenglish = orgenglish.read()
#print(contentorgenglish)
#later I will figure out how to display in two columns

#2.  access translation API:  https://tech.yandex.com/translate/
#API key:  #trnsl.1.1.20160609T174137Z.33e7da791310c9bd.e7f1d1f74c86d0ec0dfc3bf26bfdcbd21fb9f347
#translate 5 times

#original Russian translated 5 times, ends in English
from yandex_translate import YandexTranslate
translate = YandexTranslate('trnsl.1.1.20160609T174137Z.33e7da791310c9bd.e7f1d1f74c86d0ec0dfc3bf26bfdcbd21fb9f347')
firsttranslation = translate.translate(contentorgrussian, 'ru-en')
firsttranslationtext = firsttranslation['text'][0]
#getting the text out of the dictionary
secondtranslation = translate.translate(firsttranslationtext, 'en-ru')
secondtranslationtext = secondtranslation['text'][0]
thirdtranslation = translate.translate(secondtranslationtext, 'ru-en')
thirdtranslationtext = thirdtranslation['text'][0]
fourthtranslation = translate.translate(thirdtranslationtext, 'en-ru')
fourthtranslationtext = fourthtranslation['text'][0]
fifthtranslation = translate.translate(fourthtranslationtext, 'ru-en')
fifthtranslationtext = fifthtranslation['text'][0]

#original English translated 5 times, ends in Russian
from yandex_translate import YandexTranslate
translate = YandexTranslate('trnsl.1.1.20160609T174137Z.33e7da791310c9bd.e7f1d1f74c86d0ec0dfc3bf26bfdcbd21fb9f347')
firsttranslationmolnar = translate.translate(contentorgenglish, 'en-ru')
firsttranslationmolnartext = firsttranslationmolnar['text'][0]
#getting the text out of the dictionary
secondtranslationmolnar = translate.translate(firsttranslationmolnartext, 'ru-en')
secondtranslationmolnartext = secondtranslationmolnar['text'][0]
thirdtranslationmolnar = translate.translate(secondtranslationmolnartext, 'en-ru')
thirdtranslationmolnartext = thirdtranslationmolnar['text'][0]
fourthtranslationmolnar = translate.translate(thirdtranslationmolnartext, 'ru-en')
fourthtranslationmolnartext = fourthtranslationmolnar['text'][0]
fifthtranslationmolnar = translate.translate(fourthtranslationmolnartext, 'en-ru')
fifthtranslationmolnartext = fifthtranslationmolnar['text'][0]


#firsttranslation is type dict
#dict structure:  {u'lang': u'ru-en', u'text': [u'Hello, earth!'], u'code': 200}
#print(firsttranslation['text'[0]])

#print('Languages:', translate.langs)
#print('Translate directions:', translate.directions)


#3.  display poems 

print(contentorgrussian)
time.sleep(5)
print(firsttranslationtext)
time.sleep(5)
print(secondtranslationtext)
time.sleep(5)
print(thirdtranslationtext)
time.sleep(5)
print(fourthtranslationtext)
time.sleep(5)
print(fifthtranslationtext)

russianlist2 = fifthtranslationtext.split('\n')

for line in russianlist2[0:28]:
	print(line)

#for line in russianlist2(range(0,24)):
#	print(line)

for line in russianlist2[0:20]:
	print(line)

for line in russianlist2[0:16]:
	print(line)

for line in russianlist2[0:12]:
	print(line)

for line in russianlist2[0:8]:
	print(line)

for line in russianlist2[0:4]:
	print(line)

for line in russianlist2[0]:
	print(line)	
	
orgrussianlist2 = contentorgrussian.split('\n')

for line in orgrussianlist2[0:4]:
	print(line)

for line in orgrussianlist2[0:12]:
	print(line)

for line in orgrussianlist2[0:16]:
	print(line)

for line in orgrussianlist2[0:20]:
	print(line)

for line in orgrussianlist2[0:24]:
	print(line)

for line in orgrussianlist2[0:28]:
	print(line)
	

# SPARE CODE FOLLOWS; IGNORE

#to clear screen after each poem:
#import os
#os.system('cls' if os.name == 'nt' else 'clear')
    

#for line in orgrussianlist2[0:8]:
#	print(line)
#for line in orgrussianlist2[0:4]:
#	print(line)

#display 5 cycles of poems

#print(contentorgrussian, /n, firsttranslationtext, secondtranslationtext, #thirdtranslationtext, fourthtranslationtext, fifthtranslationtext)


#contentorgenglishlist = contentorgenglish.split('\n')
#contentorgrussianlist = contentorgrussian.split('\n')

#fmt = '{:>100}{}'  cool smooshed version
#fmt = '{}{:<100}'
#fmt = '{}{:>100}'
#x = 150 - len(line)

#for line in contentorgrussianlist:
#    fmt = '{:>100}{}' 
#   print(fmt.format(line, contentorgenglishlist[0]))
#   contentorgenglishlist.pop(0)
    

#firsttranslationlist = firsttranslationtext.split('\n')
#firsttranslationmolnarlist = firsttranslationmolnartext.split('\n')



    



#after the cycle has completed, visually disintegrate the last machine translation
#visually, we begin re-building the original poems until we end back at the originals

#orgrussian = open("afrussian.txt", encoding = "utf-8")
#contentorgrussian = orgrussian.read()
#print(contentorgrussian)

#orgenglish = open("afenglish.txt", encoding = "utf-8")
#contentorgenglish = orgenglish.read()
#print(contentorgenglish)



