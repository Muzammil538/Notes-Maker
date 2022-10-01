# Imports are here
import os
from time import sleep
from datetime import datetime as dt
class notesMaker ():
    global curntTime , cwd
    curntTime = dt.now()
    cwd = os.getcwd()
    def clearTermnal ():
        os.system("clear")

    # This is the function to initialise note maker
    def initNotesMaker () :
        print("Initialised")
        dirName = "Notes"
        NMDir = os.path.join(cwd,dirName)
        os.mkdir(NMDir)
        print("After the initaialisation please rerun the program")
    
    # This function takes the info for the note
    def MakeNote ():
        global ifNoteTitle
        ifNoteTitle = input("Do you have a title for your Note \n(A) Yes\t||(any letter) No (Default title)\n")
        if ifNoteTitle.lower() == "a" or ifNoteTitle.lower() == "yes":
            global noteTitle
            noteTitle = input("Enter the title of the note:\t")
        else:
            strCurntTime = dt.isoformat(curntTime)
            global Ntitle 
            Ntitle = "Notes Maker_"+strCurntTime
        sleep(2)
        global theNote
        theNote = input("Enter your Note here :\n\n")
        
    # This function stored the notes in txt file
    def storeNote ():
        if ifNoteTitle.lower() == "a":
            with open("Notes/"+noteTitle+".txt" , "w") as f:
                f.write(theNote)
            print("Your Note is saved successfully as\t"+noteTitle+".txt")
        else: 
            with open("Notes/"+Ntitle+".txt" , "w") as f:
                f.write(theNote)
            print("Your Note is saved successfully as\t"+Ntitle+".txt")
            


    print("hello! \n Welcome to the Notes Maker \n\t - By Muzammil\n")
    sleep(2)
    clearTermnal()
    askNote = input("Would you like to make a note ? \n (A) Yes \t (B) No \n")
    sleep(3)
    clearTermnal()
    if askNote.lower() == "a" or askNote.lower() == "yes" :
        print("Here you go with the notes maker!")
        initDir = cwd+"/Notes"
        isInitDir = os.path.isdir(initDir)
        if(isInitDir != True) :
            print("We need to initialise the notes maker to use it, please wait for a moment to let it initialise.")
            sleep(5)
            initNotesMaker()
        else:
            print("Here We Go!")
            sleep(2)
            MakeNote()
            print("We are storing your note")
            sleep(2)
            storeNote()

    else:
        print("Have a nice day!")


if __name__ == "__main__":
    notesMaker()