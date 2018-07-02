from functools import partial
from tkinter import *
from tkinter.ttk import Style, Frame, Button
import pyttsx3
import sys

sys.setrecursionlimit(5000)

import autocomplete
import time
autocomplete.load()

#Declaring global variables#

is_word=0
is_char=0	


index=0
temp=[]
sentence=''
word=''
char=''
take_new_input=''
store=[]
idx=0
space=0
tempkeyword1=''
tempkeyword2=''
flag = 0
st=[]
preflag=0

it1 = 0
it2 = 0
it3 = 0
it4 = 0


l1 = False
l2 = False
l3 = False
l4 = False

runningLevel_1 = False
runningLevel_2 = False
runningLevel_3 = False
runningLevel_4 = False

level1Buttons = {}
level2Buttons = {}
level3Buttons = {}
level4Buttons = {}

level1Callid = ""
level2Callid = ""
level3Callid = ""
level4Callid = ""

#End of Declaration#

def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]

def phrases():
    global index
    global temp
    global preflag
    global level3Buttons
    preflag=2
    file=open("word.txt","r")
    temp=remove_newlines("word.txt")

    temp_store=temp[index*4:(index+1)*4]
    k=1
    for keys in temp_store:
        string = str(k)
        print("phrase {} : {}".format(k,keys))
        # Changes done if-else statement added - Siddharth
        if keys=="":
            level3Buttons[k] = "empty"
        else:
            level3Buttons[k] = keys

        Main_Window._buttons4[string].config(text=keys)
        k=k+1
    if(k!=5):
        for i in range(k,5):
            string = str(i)
            level3Buttons[i] = "empty"
            Main_Window._buttons4[string].config(text="")


def add(word):
    file=open("word.txt","a+")
    file.write(word+"\n")


#--new functionalities--#

def new_more():
    global index
    global temp
    global preflag
    index=index+1
    temp_store=temp[index*4:(index+1)*4]
    if(preflag==1):
    	k=1
    	for keys in temp_store:
    		string = str(k)
	    	print("word {} : {}".format(k,keys[0]))
    		level3Buttons[k] = keys[0]
    		Main_Window._buttons4[string].config(text=keys[0])
    		k=k+1
    	if(k!=5):
    		for i in range(k,5):
    			string = str(i)
    			level3Buttons[i] = "empty"
    			Main_Window._buttons4[string].config(text="")
    elif(preflag==2):
    	k=1
    	for keys in temp_store:
    		string = str(k)
    		print("phrase {} : {}".format(k,keys))
	    	level3Buttons[k] = keys
    		Main_Window._buttons4[string].config(text=keys)
    		k=k+1
    	if(k!=5):
    		for i in range(k,5):
    			string = str(i)
    			level3Buttons[i] = "empty"
    			Main_Window._buttons4[string].config(text="")

def new_undo():
	global index
	global temp
	global preflag

	if(preflag==1):
		if(index>=1):
			index=index-1
			temp_store=temp[index*4:(index+1)*4]
			k=1
			for keys in temp_store:
				string = str(k)
				print("word {} : {}".format(k,keys[0]))
				level3Buttons[k] = keys[0]
				Main_Window._buttons4[string].config(text=keys[0])
				k=k+1  
			if(k!=5):
				for i in range(k,5):
					string = str(i)
					level3Buttons[i] = "empty"
					Main_Window._buttons4[string].config(text="") 
	elif(preflag==2):
		if(index>=1):
			index=index-1
			temp_store=temp[index*4:(index+1)*4]
			k=1
			for keys in temp_store:
				string = str(k)
				print("word {} : {}".format(k,keys))
				level3Buttons[k] = keys
				Main_Window._buttons4[string].config(text=keys)
				k=k+1  
			if(k!=5):
				for i in range(k,5):

					string = str(i)
					level3Buttons[i] = "empty"
					Main_Window._buttons4[string].config(text="")


def Sort(sub_li):
    sub_li.sort(key = lambda x: x[1],reverse=True)
    return sub_li

def next_word(word):
    global temp
    temp=[]
    for i in range(ord('a'),ord('z')+1):
    	temp=temp+autocomplete.predict(word,chr(i))

    Sort(temp)
    rem=temp
    temp=[]
    temp=[i for i in rem if i[0]!="r"]
    temp_store=temp[0:4]

    k=1
    for keys in temp_store:
    	string = str(k)
    	print("word {} : {}".format(k,keys[0]))
    	level3Buttons[k] = keys[0]
    	Main_Window._buttons4[string].config(text=keys[0])
    	k=k+1
    if(k!=5):
    	for i in range(k,5):
    		string = str(i)
    		level3Buttons[i] = "empty"
    		Main_Window._buttons4[string].config(text="")



def sel_prediction(sel):
	global index
	global temp
	global sentence
	global preflag

	temp_store=temp[index*4:(index+1)*4]
	if(preflag==1):
		sentence=sentence+temp_store[sel-1][0]
		sentence=sentence+' '
		index=0
		next_word(temp_store[sel-1][0])
	elif(preflag==2):
		sentence=sentence+temp_store[sel-1][0]
		sentence=sentence+' '
		index=0

# Level 2 Undo #

def undo():
    global sentence
    global space
    global flag

    temp=0
    for i in range(len(sentence)-2,0,-1):
        if(sentence[i]==' '):
            temp=i
            break
    if(temp==0):
        sentence=''
    else:
        sentence=sentence[:temp+1]

    flag = 0

# Level 2 Erase #

def flush():

    print("-----------flush variables------------")
    global is_word
    global is_char
    global is_first_char
    global sentence
    global word
    global char
    global take_new_input
    global idx
    global space
    global tempkeyword1
    global tempkeyword2
    global flag
    global store,st
    global preflag
    global index

    flag=0
    preflag=0
    is_word=0
    is_char=0	
    index=0
    word=''
    char=''
    take_new_input=''
    store=[]
    idx=0
    space=0
    tempkeyword1=''
    tempkeyword2=''
    st=[]


def erase():
    global is_word
    global is_char
    global is_first_char
    global sentence
    global word
    global char
    global take_new_input
    global idx
    global space
    global tempkeyword1
    global tempkeyword2
    global flag
    global store,st
    global preflag
    global index

    index=0
    flag=0
    preflag=0
    is_word=0
    is_char=0	

    sentence=''
    word=''
    char=''
    take_new_input=''
    store=[]
    idx=0
    space=0
    tempkeyword1=''
    tempkeyword2=''
    st=[]


# Selecting word from Level 3 #


def select(store,sel):
        global is_word
        global is_char
        global is_first_char
        global sentence
        global word
        global char
        global take_new_input
        global idx
        global space
        global tempkeyword1
        global tempkeyword2
        global preflag

        keyword1=tempkeyword1
        keyword2=tempkeyword2
        print("keyword 1 is:" + keyword1)
        select=sel
        if(select==1):
                if(keyword2==''):
                        word=keyword1
                        is_char=1
                        is_word=0
                        idx=0
                else:
                        word=keyword2
                        is_char=1
                        is_word=0
                        idx=0
        elif(select==2):
                        word=store[0][0]
                        keyword1=word
                        is_char=0
                        is_word=1
                        idx=0
        elif(select==3):
                        word=store[1][0]
                        keyword1=word
                        is_char=0
                        is_word=1
                        idx=0
        elif(select==4):
                        word=store[2][0]
                        keyword1=word
                        is_char=0
                        is_word=1
                        idx=0   

        tempkeyword1=keyword1
        tempkeyword2=keyword2

        if(is_word==1 or is_char==1):
                flg=0
                temp=len(sentence)
                for i in range(len(sentence)-1,0,-1):
                        if(sentence[i]==' '):   
                                temp=i
                                flg=1
                                break;
                if(flg==1):
                        sentence=sentence[:temp+1]

                sentence=sentence+word

        if(is_word==1):
            preflag=1
            sentence=sentence+' '
            next_word(word)



#Start of word prediction Function#

def word_prediction(keyword1,keyword2):   
        global is_word
        global is_char
        global is_first_char
        global sentence
        global word
        global char
        global take_new_input
        global store,st
        global idx
        global space
        global tempkeyword1
        global tempkeyword2
        global flag

        print("word prediction")
        store=autocomplete.predict(keyword1,keyword2)
        st = store
        

        if(idx==0):
                store=store[0:3]
        elif(idx>0):
                store=store[idx*3:(idx+1)*3]    
        
        if(len(store)==0):
                if(keyword2==''):
                	print("word 1:"+keyword1)
                	level3Buttons[1] = keyword1
                	Main_Window._buttons4["1"].config(text=keyword1)
                	for i in range(2,5):
                		string = str(i)
                		level3Buttons[i] ="empty"
                		Main_Window._buttons4[string].config(text="")
                else:
                	print("word 1:"+keyword2)
                	level3Buttons[1] = keyword2
                	Main_Window._buttons4["1"].config(text=keyword2)
                	for i in range(2,5):
                		string = str(i)
                		level3Buttons[i] ="empty"
                		Main_Window._buttons4[string].config(text="")
        else:
                if(keyword2==''):
                        print("word 1 : "+keyword1)
                        level3Buttons[1] = keyword1
                        Main_Window._buttons4["1"].config(text=keyword1)
                        k=2
                        for keys in store:
                        	string = str(k)
                        	print("word {} : {}".format(k,keys[0]))
                        	level3Buttons[k] = keys[0]
                        	Main_Window._buttons4[string].config(text=keys[0])
                        	k=k+1  
                        if(k!=5):
                        	for i in range(k,5):
                        		string = str(i)
                        		level3Buttons[i] = "empty"
                        		Main_Window._buttons4[string].config(text="")       
                else:
                        print("word 1 : "+keyword2)
                        level3Buttons[1] = keyword2
                        Main_Window._buttons4["1"].config(text=keyword2)
                        k=2
                        for keys in store:
                        	string = ""
                        	string = str(k)
                        	print("word {} : {}".format(k,keys[0]))
                        	level3Buttons[k] = keys[0]
                        	Main_Window._buttons4[string].config(text=keys[0])
                        	k=k+1  
                        if(k!=5):
                        	for i in range(k,5):
                        		string = ""
                        		string = str(i)
                        		level3Buttons[i] = "empty"
                        		Main_Window._buttons4[string].config(text="") 

        tempkeyword1 = keyword1
        tempkeyword2 = keyword2

def extraone():
        global is_char
        global sentence
        global space
        global flag
        global store

        for i in range(0,4):
        	string = ""
        	n = i+1
        	string = string + str(n)
        	level3Buttons[i+1] = ""
        	Main_Window._buttons4[string].config(text="")

        sentence=sentence+' '
        space=space+1
        if(is_char):
                flag = 0
                tempkeyword1=''
                tempkeyword2=''
		
                        

def extratwo():
        global take_new_input
        global tempkeyword1

        tempkeyword1=tempkeyword1+take_new_input
        word_prediction(tempkeyword1,'')


def extrathree():
                        
        global take_new_input
        global tempkeyword2

        tempkeyword2=tempkeyword2+take_new_input
        word_prediction(tempkeyword2,'')
        

def extrafour():
        global take_new_input
        global tempkeyword1

        word_prediction(tempkeyword1+take_new_input,'')



def extrafive():
        global take_new_input
        global tempkeyword1
        global isused

        if(isused==1):
                take_new_input = lower
                isused = 0
        word_prediction(tempkeyword1,take_new_input)

        
def extra():
        global is_word
        global is_char
        global sentence
        global take_new_input
        global tempkeyword1
        global tempkeyword2
        global isused

        if(isused==1):
                take_new_input = lower
                isused = 0
        print(isused)
        if(take_new_input==' '):
                extraone()
                return

        if(is_char):
                if(tempkeyword2==''):
                        extratwo()
                else:
                        extrathree()

        elif(sentence[len(sentence)-1]!=' ' and is_word==1):
                extrafour()
                
        elif(sentence[len(sentence)-1]==' ' and is_word==1):
                extrafive()

#End of word prediction Function#

               
def maininput(): 
    global take_new_input
    global isused
    global flag

    for i in range(0,1):
        if(isused==1):
                take_new_input = lower
                isused = 0
        word_prediction(take_new_input,'')
        flag = 1


# ---------------------------------------------------------------------------------------------- #
## FRONT-END -- START ##

# Functions declared to add command to buttons ! These have no use in real application but are
# necessary for buttons to work.

def level1buttons(val):
    print(val)
    pass

def level1add(val):
    print("Adding....", val)
    pass

def level2back():
    print("Doing level 2 back")
    pass

def level2undo():
    print("Undoing Level 2")
    pass

def level2speak():
    print("Speaking at level 2")
    pass

def level2buttons():
    print("Level 2 Button clicked")
    pass

def level2erase():
    print("Erase after final speak")
    pass

def level3buttons():
    print("Level 3 Button clicked")
    pass

def level3more():
    print("Level 3 More")
    pass

def level3back():
    print("Level 3 Back")
    pass

def level4text():
    print("Level 4 Text")
    pass

def level4speak():
    print("Level 4 Speak")
    pass

def level4back():
    print("Level 4 Back")
    pass

# ------------------------------------------------------------------------------------------- #

def action(event):
    print("Action Successfully Called")

    global runningLevel_1, runningLevel_2, runningLevel_3, runningLevel_4, Main_Window
    global level1Buttons, level2Buttons, level3Buttons, level4Buttons
    global it1, it2, it3, it4, l1, l2, l3, l4
    global lower, newAddedText, beforeEraseText, textToEraseIndex
    global sentence
    global level1Callid, level2Callid, level3Callid, level4Callid
    global isused, flag, sel
    global tempkeyword1,tempkeyword2,idx,store,preflag,temp	


    if l1:
        # Level 1 action
        print("Inside L1")
        if it1==1:
            # Level 1 ADD
            root.after_cancel(level1Callid)
            runningLevel_1 = False
            l1 = False
            Main_Window._buttons1[level1Buttons[(it1 - 1) % 11]].config(style="b1.TButton")
            phrases()

            runningLevel_3 = True
            it3 = 0

            root.update()

            return scanningLevel_3()

        else:
            root.after_cancel(level1Callid)
            runningLevel_1 = False
            l1 = False

            if it1 == 0:
                sys.exit()
            else:
                val = level1Buttons[(it1-1)%11]

            if it1 == 0:
                Main_Window._buttons1[level1Buttons[10]].config(style="b1.TButton")
            else:
                Main_Window._buttons1[level1Buttons[(it1 - 1) % 11]].config(style="b1.TButton")

            level2Buttons[1] = val[0]
            level2Buttons[2] = val[1]
            level2Buttons[3] = val[2]

            Main_Window._buttons2["1"].config(text=val[0])
            Main_Window._buttons2["2"].config(text=val[1])
            Main_Window._buttons2["3"].config(text=val[2])

            runningLevel_2 = True
            it2 = 0
            root.update()
            return scanningLevel_2()

    elif l2:

        # Level 2 action
        print("Inside L2")
        if it2 == 0:
            # Erase function of Level 2 #

            erase()
            level4Buttons[0] = sentence 
            Main_Window._buttons5["Text"].config(text=level4Buttons[0])

            root.update()


        elif it2 == 1:
            # Back function

            root.after_cancel(level2Callid)

            runningLevel_2 = False
            l2 = False
            Main_Window._buttons2[level2Buttons[0]].config(style="b1.TButton")

            runningLevel_1 = True
            it1 = 0

            root.update()

            return scanningLevel_1()

        elif it2<=4:

            root.after_cancel(level2Callid)

            runningLevel_2 = False
            l2 = False
            Main_Window._buttons2[str(it2 - 1)].config(style="b1.TButton")

            val2 = level2Buttons[(it2 - 1) % 5]
            upper = ord(val2)
            lower = chr(upper + 32)
            isused = 1

            if(val2=='#'):
                lower = ' '
                level4Buttons[0] = level4Buttons[0] + ' '

                if(flag==0):
                	maininput()
                elif(flag==1):
                	extra()
                
                runningLevel_2 = True
                it2 = 0
                
                root.update()
                return scanningLevel_2()

            else:
                if(flag==0):
                	maininput()
                elif(flag==1):
                	extra()

                runningLevel_3 = True
                it3 = 0
                root.update()
                return scanningLevel_3()

        elif it2==5:
            # Define level 2 undo operation #
            undo()
            level4Buttons[0] = sentence
            Main_Window._buttons5["Text"].config(text=level4Buttons[0])

            root.update()

        elif it2==6:

            # Define level 2 speak operation #
            engine.say(sentence)
            engine.runAndWait()
            pass


    elif l3:

        # Level 3 action

        if it3 == 1:
            flush()
            root.after_cancel(level3Callid)

            # Back Function
            runningLevel_3 = False
            l3 = False
            Main_Window._buttons4[level3Buttons[6]].config(style="b2.TButton")

            runningLevel_2 = True
            it2 = 0

            root.update()

            return scanningLevel_2()

            
        elif it3<=5:
            # Add 1,2,3 and 4 predicted words to speak text box in level 4
            sel = it3-1
            if(preflag==0):
            	select(store,sel)
            else:
            	sel_prediction(sel)
            level4Buttons[0]=sentence
            Main_Window._buttons5["Text"].config(text=sentence)
            print("FINAL SENTENCE : "+sentence)

            root.update()

            
        elif it3==6:
            # Add MORE function of level 3 and update level3Buttons[0,1,2,3,4] values
            # pass

            #=========LEVEL 3: more========#
            if(preflag==0):
            	if(len(st)-len(store)>=1):
            		idx=idx+1
            		word_prediction(tempkeyword1,tempkeyword2)
            else:
            	if(len(temp)-index*4>=1):
            		new_more()                    

            root.update()

        """    
        elif it3==7:

            #+++++++LEVEL 3: undo+++++++++#
            if(preflag==0):
            	if(idx>0):
            		idx=idx-1
            		word_prediction(tempkeyword1,tempkeyword2)  
            else:
            	if(index>0):
            		new_undo()

            root.update()
        """

        """
        elif it3==8:
            # Speak Function - Move to level 4
            #+++++++LEVEL 3: speak+++++++++#


            for i in range(1,5):
                    print(level3Buttons[i])
                    engine.say(level3Buttons[i])
                    engine.runAndWait()
            
            level4Buttons[0]=sentence
            root.after_cancel(level3Callid)

            runningLevel_3 = False
            l3 = False
            Main_Window._buttons4[level3Buttons[7]].config(style="b2.TButton")

            runningLevel_4 = True
            it4 = 1

            root.update()

            return scanningLevel_4()
        """

    elif l4:
        # Level 4 action
        print("Inside L4")
        if it4 == 1:

            root.after_cancel(level4Callid)

            runningLevel_4 = False
            l4 = False
            Main_Window._buttons5[level4Buttons[2]].config(style="b3.TButton")

            runningLevel_3 = True
            it3 = 0

            root.update()

            return scanningLevel_3()

        elif it4 == 2:
            # Function to speak final sentence, pass level4Buttons[0] to speak module

            engine.say(sentence)
            engine.runAndWait()
            
            root.update()


"""
# -------------------------------------------------------------------------------------------#
# START SCANNING FUNCTION 

def startScanning():
    global runningLevel_1
    global level1Callid, level2Callid, level3Callid, level4Callid

    runningLevel_1 = True
    return scanningLevel_1()

# -------------------------------------------------------------------------------------------#
# STOP SCANNING FUNCTION

def stopScanning():

    global runningLevel_1, runningLevel_2, runningLevel_3, runningLevel_4, Main_Window
    global level1Buttons, level2Buttons, level3Buttons, level4Buttons
    global it1, it2, it3, it4, l1, l2, l3, l4
    global level1Callid, level2Callid, level3Callid, level4Callid

    root.after_cancel(level1Callid)
    root.after_cancel(level2Callid)
    root.after_cancel(level3Callid)
    root.after_cancel(level4Callid)


    runningLevel_1 = False
    runningLevel_2 = False
    runningLevel_3 = False
    runningLevel_4 = False

    l1 = False
    l2 = False
    l3 = False
    l4 = False

    if it1 == 0:
        Main_Window._buttons1[level1Buttons[10]].config(style="b1.TButton")
    else:
        Main_Window._buttons1[level1Buttons[(it1-1)%11]].config(style="b1.TButton")

    if it2 == 0:
        Main_Window._buttons3[level2Buttons[6]].config(style="b1.TButton")
    elif it2<=4:
        if it2-1==0:
            Main_Window._buttons2[level2Buttons[0]].config(style="b1.TButton")
        else:
            Main_Window._buttons2[str((it2-1)%7)].config(style="b1.TButton")
    elif it2>4:
        Main_Window._buttons3[level2Buttons[(it2-1)%7]].config(style="b1.TButton")

    if it3 == 0:
        Main_Window._buttons4[level3Buttons[8]].config(style="b2.TButton")
    elif it3 == 1:
        Main_Window._buttons4[level3Buttons[0]].config(style="b2.TButton")
    elif it3<=5:
        Main_Window._buttons4[str(it3 - 1)].config(style="b2.TButton")
    else:
        Main_Window._buttons4[level3Buttons[it3-1]].config(style="b2.TButton")

    if it4 == 0:
        Main_Window._buttons5["Back"].config(style="b3.TButton")
    elif it4 == 2:
        Main_Window._buttons5["Speak"].config(style="b3.TButton")

    Main_Window._buttons2["1"].config(text="")
    Main_Window._buttons2["2"].config(text="")
    Main_Window._buttons2["3"].config(text="")
    Main_Window._buttons4["Words"].config(text="Words")
    Main_Window._buttons4["1"].config(text="")
    Main_Window._buttons4["2"].config(text="")
    Main_Window._buttons4["3"].config(text="")
    Main_Window._buttons4["4"].config(text="")
    Main_Window._buttons5["Text"].config(text="")

    #print(it1)

    it1 = 0
    it2 = 0
    it3 = 0
    it4 = 0

    root.update()
    root.destroy()
    sys.exit(0)
"""

# -------------------------------------------------------------------------------------------#
# SCANNING LEVEL 1 FUNCTION 

def scanningLevel_1():

    global runningLevel_1, Main_Window, it1, l1, level1Callid, level1Buttons

    if runningLevel_1:

        # Scans over level 1 buttons
        #print(level1Buttons[0])
        l1 = True

        if it1 == 0:
            Main_Window._buttons1[level1Buttons[10]].config(style="b4.TButton")
            Main_Window._buttons1[level1Buttons[0]].config(style = "b44.TButton")
        else:
            Main_Window._buttons1[level1Buttons[(it1-1)%11]].config(style="b4.TButton")
            Main_Window._buttons1[level1Buttons[it1]].config(style="b44.TButton")

        root.update()

        # Add modifies voice here for level 1
        emptystr = level1Buttons[it1][0] + ' ' + level1Buttons[it1][1] + ' ' + level1Buttons[it1][2]

        if(it1==0):
            engine.say(level1Buttons[it1])
            engine.runAndWait()
            #print(level1Buttons[it1])

        elif(it1<10):
            engine.say(emptystr)
            #print(emptystr)
            engine.runAndWait()

        elif it1==10:
            engine.say(level1Buttons[it1])
            engine.runAndWait()
        ####################################

        it1 = (it1 + 1) % 11
        level1Callid = root.after(2000, scanningLevel_1)

# -------------------------------------------------------------------------------------------#
# SCANNING LEVEL 2 FUNCTION 

def scanningLevel_2():

    global runningLevel_2, Main_Window, it2, l2, level2Callid, level2Buttons

    if runningLevel_2:

        l2 = True
        # Scans over level 2 buttons
        if it2 == 0:
            Main_Window._buttons3[level2Buttons[6]].config(style="b1.TButton")
            Main_Window._buttons2[level2Buttons[0]].config(style = "b11.TButton")
        elif it2 < 4:
            if (it2-1)%7 == 0:
                Main_Window._buttons2[level2Buttons[0]].config(style="b1.TButton")
                Main_Window._buttons2[str(it2)].config(style="b11.TButton")
            else:
                Main_Window._buttons2[str((it2 - 1) % 7)].config(style="b1.TButton")
                Main_Window._buttons2[str(it2)].config(style="b11.TButton")
        elif it2 == 4:
            Main_Window._buttons2["3"].config(style="b1.TButton")
            Main_Window._buttons3[level2Buttons[4]].config(style="b11.TButton")
        elif it2 > 4:
            Main_Window._buttons3[level2Buttons[(it2-1)%7]].config(style="b1.TButton")
            Main_Window._buttons3[level2Buttons[it2]].config(style="b11.TButton")

        root.update()

        # Add modified voice here for level 2 #
        engine.say(level2Buttons[it2])
        engine.runAndWait()
        ######################################

        it2 = (it2 + 1) % 7
        level2Callid = root.after(2000, scanningLevel_2)

# -------------------------------------------------------------------------------------------#
# SCANNING LEVEL 3 FUNCTION 

def scanningLevel_3():

    global runningLevel_3, Main_Window, it3, l3, level3Callid, level3Buttons

    if runningLevel_3:

        # Scans over level 2 buttons
        l3 = True

        if it3==1:
            Main_Window._buttons4[level3Buttons[6]].config(style="b2.TButton")
            Main_Window._buttons4[str(1)].config(style="b33.TButton")

        elif it3<=4 and it3!=0:
            Main_Window._buttons4[str(it3-1)].config(style="b2.TButton")
            Main_Window._buttons4[str(it3)].config(style="b33.TButton")

        elif it3==5:
            Main_Window._buttons4[str(it3-1)].config(style="b2.TButton")
            Main_Window._buttons4[level3Buttons[5]].config(style="b33.TButton")

        elif it3!=0:
            Main_Window._buttons4[level3Buttons[it3-1]].config(style="b2.TButton")
            Main_Window._buttons4[level3Buttons[it3]].config(style="b33.TButton")

        root.update()

    
        # Add modified Voice Here for level 3 #
        engine.say(level3Buttons[it3])
        engine.runAndWait()
        ######################################

        it3 = (it3 + 1) % 7

        if it3 == 0:
            it3 = 1
        level3Callid = root.after(2000, scanningLevel_3)

# -------------------------------------------------------------------------------------------#
# SCANNING LEVEL 4 FUNCTION 

def scanningLevel_4():

    global runningLevel_4, Main_Window, it4, l4, level4Callid
    global sentence

    if runningLevel_4:

        # Scans over level 2 buttons
        l4 = True

        if it4 == 1:
            Main_Window._buttons5[level4Buttons[2]].config(style="b3.TButton")
            Main_Window._buttons5[level4Buttons[1]].config(style="b34.TButton")

        elif it4 == 2:
            Main_Window._buttons5[level4Buttons[1]].config(style="b3.TButton")
            Main_Window._buttons5[level4Buttons[2]].config(style="b34.TButton")

        root.update()

        if(level4Buttons[0]==''):
        	level4Buttons[0]="empty"

        # Add modified voice here for level 4 #
        engine.say(level4Buttons[it4])
        engine.runAndWait()
        ######################################

        it4 = (it4 + 1) % 3

        if it4 == 0:
            it4 = 1
        level4Callid = root.after(2000, scanningLevel_4)


# -------------------------------------------------------------------------------------------#
# Class declaration to Initialize all necessary buttons 

class InitializeWindow:

    def __init__(self, master):

        self._master = master
        self._level1 = ["ADD", "ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZ#", "QUIT"]

        #self._buttons0 = {}
        self._buttons1 = {}
        self._buttons2 = {}
        self._buttons3 = {}
        self._buttons4 = {}
        self._buttons5 = {}

        #self._frame0 = Frame(master, padding = (11,10,0,0))
        self._frame1 = Frame(master, padding = (0,10,0,0))
        self._topframe234 = Frame(master, padding = (32, 16, 32, 0))
        self._frame2 = Frame(self._topframe234)
        self._frame3 = Frame(self._topframe234)
        self._frame4 = Frame(self._topframe234, width = 200)
        self._frame5 = Frame(master, relief = "ridge", width = 100, height = 50)
        self.initUI()

    # initUI method of InitializeWindow #
    def initUI(self):

        # Packing Frames in Root window #
        global level1Buttons, level2Buttons, level3Buttons, level4Buttons

        self._master.title("HOPE")
        self._master.bind('<Button-1>', action)

        #self._frame0.pack(anchor = N)
        self._frame1.pack(anchor = N)
        self._topframe234.pack(anchor = W, fill = X)
        self._frame2.pack(side = LEFT)
        self._frame3.pack(side = RIGHT)
        self._frame4.pack(anchor = CENTER, pady = 5)
        self._frame5.pack(anchor = CENTER)

        # Style configuration for Buttons #

        # Style for level 1 and 2 #
        s1 = Style()
        s1.configure("b1.TButton", font=("Helvetica", 9, "bold"), foreground="#154360",
                     background="#aed6f1", padding=2)

        # Style for level 3 #
        s2 = Style()
        s2.configure("b2.TButton", font=("Helvetica", 9, "bold"), foreground="#17202a",
                     background="#f8f9f9", padding=2, borderwidth=0)

        # Style for level 0 and 4 #
        s3 = Style()
        s3.configure("b3.TButton", font=("Helvetica", 9, "bold"), foreground="#186a3b",
                     background="#eafaf1", padding=2)

        s4 = Style()
        s4.configure("b4.TButton", font=("Helvetica", 9, "bold"), foreground="#154360",
                     background="#aed6f1", padding=2)


        """# Level 0 Button Initialization #

        self._buttons0["StartScan"] = (Button(self._frame0, text="Start Scan", style="b3.TButton"))
        self._buttons0["StartScan"].configure(command=startScanning)
        self._buttons0["StartScan"].pack(side = LEFT, padx = 2)

        self._buttons0["StopScan"] = (Button(self._frame0, text="Stop Scan", style="b3.TButton"))
        self._buttons0["StopScan"].configure(command=stopScanning)
        self._buttons0["StopScan"].pack(side = LEFT, padx=2)"""

        # Level 1 Button Initialization #

        for i, val in enumerate(self._level1):

            self._buttons1[val] = (Button(self._frame1, text = val, style = "b4.TButton"))
            level1Buttons[i] = val

            if val=="ADD":
                self._buttons1[val].configure(command = partial(level1add, val))
            elif val=="QUIT":
                self._buttons1[val].configure(command = quit)
            else:
                self._buttons1[val].configure(command=partial(level1buttons, val))

            self._buttons1[val].pack(side = LEFT, padx = 1)


        # Level 2 Button Initialization #

        self._buttons2["Back"] = (Button(self._frame2, text = "Back", style = "b1.TButton"))
        self._buttons2["Back"].configure(command = level2back)
        self._buttons2["Back"].pack(pady = 2)
        level2Buttons[0] = "Back"

        self._buttons2["1"] = (Button(self._frame2, style="b1.TButton"))
        self._buttons2["1"].configure(command=partial(level2buttons))
        self._buttons2["1"].pack(pady = 2)
        level2Buttons[1] = "empty"

        self._buttons2["2"] = (Button(self._frame2, style="b1.TButton"))
        self._buttons2["2"].configure(command=level2buttons)
        self._buttons2["2"].pack(pady = 2)
        level2Buttons[2] = "empty"

        self._buttons2["3"] = (Button(self._frame2, style="b1.TButton"))
        self._buttons2["3"].configure(command=level2buttons)
        self._buttons2["3"].pack(pady = 2)
        level2Buttons[3] = "empty"

        self._buttons3["Undo"] = (Button(self._frame3, text = "Undo", style="b1.TButton"))
        self._buttons3["Undo"].configure(command=level2undo)
        self._buttons3["Undo"].pack(pady = 2)
        level2Buttons[4] = "Undo"

        self._buttons3["Speak"] = (Button(self._frame3, text = "Speak", style="b1.TButton"))
        self._buttons3["Speak"].configure(command=level2speak)
        self._buttons3["Speak"].pack(pady = 2)
        level2Buttons[5] = "Speak"

        self._buttons3["Erase"] = (Button(self._frame3, text = "Erase", style="b1.TButton"))
        self._buttons3["Erase"].configure(command=level2erase)
        self._buttons3["Erase"].pack(pady = 2)
        level2Buttons[6] = "Erase"


        # Level 3 Button Initialization #

        self._buttons4["Words"] = (Button(self._frame4, text = "Words", style="b2.TButton", width = 80))
        self._buttons4["Words"].configure(command=level3buttons)
        self._buttons4["Words"].pack(pady = 2)
        level3Buttons[0] = "Words"

        self._buttons4["1"] = (Button(self._frame4, style="b2.TButton", width = 80))
        self._buttons4["1"].configure(command=level3buttons)
        self._buttons4["1"].pack(pady = 2)
        level3Buttons[1] = "empty"

        self._buttons4["2"] = (Button(self._frame4, style="b2.TButton", width = 80))
        self._buttons4["2"].configure(command=level3buttons)
        self._buttons4["2"].pack(pady = 2)
        level3Buttons[2] = "empty"

        self._buttons4["3"] = (Button(self._frame4, style="b2.TButton", width = 80))
        self._buttons4["3"].configure(command=level3buttons)
        self._buttons4["3"].pack(pady = 2)
        level3Buttons[3] = "empty"

        self._buttons4["4"] = (Button(self._frame4, style="b2.TButton", width = 80))
        self._buttons4["4"].configure(command=level3buttons)
        self._buttons4["4"].pack(pady = 2)
        level3Buttons[4] = "empty"

        self._buttons4["More"] = (Button(self._frame4, text = "More", style="b2.TButton", width=20))
        self._buttons4["More"].configure(command=level3more)
        self._buttons4["More"].pack(side = LEFT, pady = 6, padx = 105)
        level3Buttons[5] = "More"

        """
        self._buttons4["Undo"] = (Button(self._frame4, text="Undo", style="b2.TButton", width=20))
        self._buttons4["Undo"].configure(command=level3more)
        self._buttons4["Undo"].pack(side=LEFT, pady=6, padx=2)
        level3Buttons[6] = "Undo"

        self._buttons4["Speak"] = (Button(self._frame4, text="Speak", style="b2.TButton", width=20))
        self._buttons4["Speak"].configure(command=level3more)
        self._buttons4["Speak"].pack(side=LEFT, pady=6, padx=2)
        level3Buttons[7] = "Speak"
        """

        self._buttons4["Back"] = (Button(self._frame4, text = "Back", style="b2.TButton", width=20))
        self._buttons4["Back"].configure(command=level3back)
        self._buttons4["Back"].pack(side = LEFT, pady = 6, padx = 80)
        level3Buttons[6] = "Back"


        # Level 4 Button Initialization #

        self._buttons5["Text"] = (Button(self._frame5, width = 60, style = "b3.TButton"))
        self._buttons5["Text"].configure(command = level4text)
        self._buttons5["Text"].pack(side = LEFT)
        level4Buttons[0] ="" #Store formed words if selected, in this and pass it to function action

        self._buttons5["Speak"] = (Button(self._frame5, text = "Speak", width=10, style="b3.TButton"))
        self._buttons5["Speak"].configure(command=level4speak)
        self._buttons5["Speak"].pack(side=LEFT)
        level4Buttons[1] = "Speak"

        self._buttons5["Back"] = (Button(self._frame5, text = "Back", width=10, style="b3.TButton"))
        self._buttons5["Back"].configure(command=level4back)
        self._buttons5["Back"].pack(side=LEFT)
        level4Buttons[2] = "Back"

        return self


# -------------------------------------------------------------------------------------------#
# Main function of calling frontend

if __name__ == "__main__":

    # Creating our root of Tkinter #
    root = Tk()
    root.geometry("{0}x500+0+0".format(root.winfo_screenwidth()))
    engine = pyttsx3.init()

    # Styles defined for buttons and other things when scanning occurs #
    s1 = Style()
    s1.configure("b1.TButton", font=("Helvetica", 9, "bold"), foreground="#154360",
                 background="#aed6f1", padding=2)
    s11 = Style()
    s11.configure("b11.TButton", font=("Helvetica", 9, "bold"), foreground="#ebf5fb",
                  background="#154360", padding=2)

    s2 = Style()
    s2.configure("b2.TButton", font=("Helvetica", 9, "bold"), foreground="#17202a",
                 background="#f8f9f9", padding=2, borderwidth=0)


    s3 = Style()
    s3.configure("b3.TButton", font=("Helvetica", 9, "bold"), foreground="#186a3b",
                 background="#eafaf1", padding=2)

    # Style for scanning level 3 #
    s33 = Style()
    s33.configure("b33.TButton", font=("Helvetica", 9, "bold"), foreground="#f8f9f9",
                  background="#17202a", padding=2)

    # Style for scanning level 4 #
    s34 = Style()
    s34.configure("b34.TButton", font=("Helvetica", 9, "bold"), foreground="#eafaf1",
                  background="#186a3b", padding=2)

    s4 = Style()
    s4.configure("b4.TButton", font=("Helvetica", 9, "bold"), foreground="#154360",
                 background="#aed6f1", padding=2)

    s44 = Style()
    s44.configure("b44.TButton", font=("Helvetica", 9, "bold"), foreground="#ebf5fb",
                  background="#154360", padding=2)
    # Main Loop to initialize window and start the application #
    Main_Window = InitializeWindow(root)
    runningLevel_1 = True
    scanningLevel_1()
    root.mainloop()
