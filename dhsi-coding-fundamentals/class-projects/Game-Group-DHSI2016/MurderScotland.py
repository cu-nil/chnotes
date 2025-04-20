"""MURDER IN THE SCOTTISH BORDERS: A CHOOSE YOUR OWN ADVENTURE GAME
Author: Chelsea Hartlen
Code borrowed and edited from: http://inventwithpython.com/extra/dragon2.py

Murder in the Scottish Borders is a 'Choose Your Own
Adventure' game that will let students in HIST 2200 experience the
proceedings of a murder trial in sixteenth-century Scotland.

The game ends when the player: is executed, purchases a pardon or 
is acquitted."""

#This function defines choice options and is customisable.  'if' condition can be augmented to include, 3, 4, 5 options and so on.
def choosePath(numberOfPaths):
    choice = 0
    #Defines range of choices available to player
    while choice < 1 or choice > numberOfPaths:
    	#Prints the available input options for the user to select.
        print('1 to ' + str(numberOfPaths) + '> ', end='')
        choice = input()
        #Prompts player to choose number within defined range until player complies. Lopps back to beginnging of choosePath function.
        if choice != '1' and choice != '2':
            choice = 0
        #Sets 'choice' variable to player input.
        if choice == '1' or choice == '2':
            choice = int(choice)
    print()
    return choice

#Prompt pauses game and allows for 'choiceless' player input to continue. Prompts player to hit the return key and requires no int or str to satisfy
def pause():
    print('Press ENTER to continue.')
    input()

"""Episode or scenario "screens".  Each function contains a small narrative, prompt and input.  At the end, according to value returned by choosePath,
the function will call up another episode funtion."""

def intro():
	print()
	print()
	print(''' _______           _______  ______   _______  _______   _________ _         _________          _______    ______   _______  _______  ______   _______  _______  _______ 
(       )|\     /|(  ____ )(  __  \ (  ____ \(  ____ )  \__   __/( (    /|  \__   __/|\     /|(  ____ \  (  ___ \ (  ___  )(  ____ )(  __  \ (  ____ \(  ____ )(  ____ \
  | () () || )   ( || (    )|| (  \  )| (    \/| (    )|     ) (   |  \  ( |     ) (   | )   ( || (    \/  | (   ) )| (   ) || (    )|| (  \  )| (    \/| (    )|| (    \/
| || || || |   | || (____)|| |   ) || (__    | (____)|     | |   |   \ | |     | |   | (___) || (__      | (__/ / | |   | || (____)|| |   ) || (__    | (____)|| (_____ 
| |(_)| || |   | ||     __)| |   | ||  __)   |     __)     | |   | (\ \) |     | |   |  ___  ||  __)     |  __ (  | |   | ||     __)| |   | ||  __)   |     __)(_____  )
| |   | || |   | || (\ (   | |   ) || (      | (\ (        | |   | | \   |     | |   | (   ) || (        | (  \ \ | |   | || (\ (   | |   ) || (      | (\ (         ) |
| )   ( || (___) || ) \ \__| (__/  )| (____/\| ) \ \__  ___) (___| )  \  |     | |   | )   ( || (____/\  | )___) )| (___) || ) \ \__| (__/  )| (____/\| ) \ \__/\____) |
|/     \|(_______)|/   \__/(______/ (_______/|/   \__/  \_______/|/    )_)     )_(   |/     \|(_______/  |/ \___/ (_______)|/   \__/(______/ (_______/|/   \__/\_______)
                                                                                                                                                                        ''')
	print()
	print()
	print('''    It is 1535 and you are in the Scottish Borders.  For two 
decades your family, the Armstrongs, have been feuding with the Humes.  
Recently, you accompanied a raiding party into Hume lands as part of a cattle
raid. But the Humes were waiting.  A fight broke out between both sides and you
killed Alexander Hume, the eldest son of Archibald Hume.  Although your party 
escaped with no further casualties, the Humes reported the murder and you are
now accused (delated) of 'slauchter and murther'.  If convicted, the justiciar
will sentence you to death and all your moveable (belongings) and unmoveable 
goods (land) will be forfeited to the Crown!''')
	print()
	pause()
	intro2()

def intro2():
	print('''    In the next few minutes, you will make a series of choices
that will decide your fate.  Justice in Scotland was deeply influenced by the 
identity of the offender, kin relations and social attitudes towards violence.
The justiciary court hears felony cases.  This is where you start.  Your choices
will decide whether you succeed in securing a pardon from the king, receive an 
acquittal or receive the death penalty...''')
	print()
	print('GOOD LUCK!')
	print()
	pause()
	surety()


def surety():
    print('''    You can delay your trial if a respected member of society can 
vouch for your appearance before the court (or else be fined!).
Can someone you know promise to bring you to Edinburgh for a trial
in the next few weeks?''')
    print()
    print('  1 Yes, my father will bring me to court or pay the price.')
    print('  2 No, there is no one to be my guarantor.')
    #assigns value to path and limits the available inputs.  Then returns value
    #through choosePath and calls chosen function.
    path = choosePath(2)
    if path == 1:
        status()
    if path == 2:
        skipToTrial()

def status():
    print('''    You now have some time to try and get out of this mess.
You should request a remission (pardon) from the king.  Tell
me, what is your social standing?''')
    print()
    print('  1 I am a person of great wealth and status!')
    print('  2 I am a humble tenant farmer with a large family to feed.')
    path = choosePath(2)
    if path == 1:
        pardon()
    if path == 2:
    	poorHume()
        
def pardon():
    print('''    The king will hear your plea.  In the meantime, you can 
also see if the Humes will accept assythement (reparations).
Do you want to wait to hear about the remission or offer money
to the Humes?''')
    print()
    print('  1 I am confident in the pardon. I shall wait for news.')
    print('  2 I would like to resolve this quickly. PAY THEM OFF!')
    path = choosePath(2)
    if path == 1:
        waitPardon()
    if path == 2:
        payHume()

def poorHume():
	print('''    You do not have enough money or status to get a pardon.  
Would you like to try to pay assythement (reparations) to the
Hume family?''')
	print()
	print('  1  Yes, I have little but I must try.')
	print('  2  No, I haven\'t got enough to pay them. Why bother?')
	path = choosePath(2)
	if path == 1:
		stillPoorTrial()
	if path == 2:
		noHume()

def stillPoorTrial():
	print('    You are still too poor and must go to trial.')
	print()
	print('  Make the journey to Edinburgh to stand before the justiciar.')
	print()
	pause()
	trial()
	'''path = choosePath(1)
	if path == 1:
		trial()'''

def noHume():
   print('''    Since you have decided not to offer assythement to the
Hume family, you must go to trial.  Too bad, they might have accepted.''')
   print()
   print('  Make the journey to Edinburgh to stand before the justiciar.')
   print()
   pause()
   trial()
   '''path = choosePath(1)
   if path == 1:
   		trial()'''

def waitPardon():
	print('''    Due to your influential connections and wealth, the king sees
fit to forgive you.  It cost you 500 Pounds Scots, but you are alive.''')
	print()
	print('    Congratulations, you SECURED A PARDON!')
	print()
	print('    Would you like to play again?')
	print()
	print('  1 Yes, please!')
	print('  2 No, once was enough!')
	path = choosePath(2)
	if path == 1:
		intro()
	if path == 2:
		end()

def payHume():
	print('''    The Humes do not want anything to do with your family or your
money. Fortunately, due to your influential connections and wealth, 
the king sees fit to forgive you. It cost you 500 Pounds Scots, but
you are alive.''')
	print()
	print('    Congratulations, you SECURED A PARDON!')
	print()
	print('    Would you like to play again?')
	print()
	print('  1 Yes, please!')
	print('  2 No, once was enough!')
	path = choosePath(2)
	if path == 1:
		intro()
	if path == 2:
		end()

def skipToTrial():
	print('    You must stand trial today.')
	print()
	print('  Make your way to Edinburgh to stand before the justiciar.')
	print()
	pause()
	trial()
	'''path = choosePath(1)
	if path == 1:
		trial()'''

def trial():
	print('''    It is the day of the trial.  Before the proceedings begin,
the Earl of Douglas steps forward and claims his right of regality.
That is, he demands the right to try any of his tenants here accused of a 
crime in his own local court.  Do you hold your lands from him?''')
	print()
	print('  1 Yes, my family have held lands from him for generations.')
	print('  2 No, I am not one of his tenants.')
	path = choosePath(2)
	if path == 1:
		saveDouglas()
	if path == 2:
		failDouglas()

def saveDouglas():
	print('''    The Earl of Douglas claims the right to try you in his court.
However, he ALSO hates the Humes and needs good raiders.  He rigs 
the local trial and acquits you of the crime.''')
	print()
	print('    Congratulations, you LIVED!')
	print()
	print('    Would you like to play again?')
	print()
	print('  1 Yes, please!')
	print('  2 No, once was enough!')
	path = choosePath(2)
	if path == 1:
		intro()
	if path == 2:
		end()

def failDouglas():
	print('''    You are not his tenant and so must be tried by the justiciary court.
Do you know anyone on the assize (jury)?''')
	print()
	print('  1 Yes, my uncle is a very influential burgess of Edinburgh.')
	print('  2 No, I have no influential family in the city.')
	path = choosePath(2)
	if path == 1:
		juryWin()
	if path == 2:
		juryFail()

def juryWin():
	print('''    Your uncle is an influential member of the assize.  He bribes
the other members to acquit you.''')
	print()
	print('    Congratulations, you LIVED!')
	print()
	print('    Would you like to play again?')
	print()
	print('  1 Yes, please!')
	print('  2 No, once was enough!')
	path = choosePath(2)
	if path == 1:
		intro()
	if path == 2:
		end()	

def juryFail():
	print('''    The assize was your last chance.  Unfortunately, none of the
members know you and there are a good number of Hume men deciding
your fate.  You are sentenced to death.  Are you a man or a woman?''')
	print()
	print('  1 I am male.')
	print('  2 I am female.')
	path = choosePath(2)
	if path == 1:
		maleDeath()
	if path == 2:
		femaleDeath()

def maleDeath():
	print('''    You are hanged and all your property is forfeited to the
crown, leaving your heirs with nothing.  They fall into destitution and
live out the rest of their days under the shadow of your crime.''')
	print()
	print('    Sorry, you have been EXECUTED.')
	print()
	print('    Would you like to play again?')
	print()
	print('  1 Yes, please!')
	print('  2 No, once was enough!')
	path = choosePath(2)
	if path == 1:
		intro()
	if path == 2:
		end()

def femaleDeath():
	print('''    You are drowned and all your property is forfeited to the
crown.  Thankfully, as a woman, you did not own very much, so
your family is sad, but not entirely destitute.  You go down in
history as an inconvenient, but otherwise unnoteworthy woman.''')
	print()
	print('    Sorry, you have been EXECUTED.')
	print()
	print('    Would you like to play again?')
	print()
	print('  1 Yes, please!')
	print('  2 No, once was enough!')
	path = choosePath(2)
	if path == 1:
		intro()
	if path == 2:
		end()

def end():
	print('''                            _________          _______    _______  _        ______                              
                            \__   __/|\     /|(  ____ \  (  ____ \( (    /|(  __  \                             
                               ) (   | )   ( || (    \/  | (    \/|  \  ( || (  \  )                            
 _____  _____  _____  _____    | |   | (___) || (__      | (__    |   \ | || |   ) | _____  _____  _____  _____ 
(_____)(_____)(_____)(_____)   | |   |  ___  ||  __)     |  __)   | (\ \) || |   | |(_____)(_____)(_____)(_____)
                               | |   | (   ) || (        | (      | | \   || |   ) |                            
                               | |   | )   ( || (____/\  | (____/\| )  \  || (__/  )                            
                               )_(   |/     \|(_______/  (_______/|/    )_)(______/                             
                                                                                                                ''')
#START GAME
intro()