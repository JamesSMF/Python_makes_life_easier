from tkinter import *
from tkinter.ttk import *
import re
import os
from collections import OrderedDict
from datetime import datetime, date, time, timedelta

################### FUNCTIONS #####################

# Given a date, it finds the next weekday (e.g. next Monday).
# d: datetime      weekday: int         return: datetime
def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this     week
        days_ahead += 7
    return d + timedelta(days_ahead)

# This function returns the length of the longest value in the dict()
# It takes a dict input and returns an int
def longestName(theDic):
    longest = max(theDic.values(), key=len)
    return len(longest)

# This function takes an input of ordered dict() and sort it by key (FST in PAIR)
def sortDict(assignment):
    assignment = OrderedDict(sorted(assignment.items(), key=lambda x: int(x[0])))


################### GUI CODE #######################

root = Tk()
root.geometry("960x710")
# root.resizeable(0,0)

# analysis by James: This initializes the app frame size.
bigFrame = Frame(root, width = 960, height = 710, relief = "raise")
bigFrame.grid()
bigFrame.place

############### BACKEND CODE #################

# -------------- Start-up Preparition -------------- #

assignment = dict()   # restructured: map from due dates to assignment
if os.stat("DataBase.db").st_size != 0:
    inputFile = open("DataBase.db", "r")
    for line in inputFile:
        newString = line.split()     # split lines in database by space
        the_name_of_assignment = ' '.join(newString[1:])    # newString[0] is date and time
        assignment[newString[0]] = the_name_of_assignment   # map date and time to name
    # end for
# end if

# get today's date
tDate = datetime.today()
todayDate = int(tDate.strftime('%Y%m%d'))

# push next week's agenda in
if os.stat("Weekly.db").st_size != 0:
    nextWeek = open("Weekly.db", "r")
    for line in nextWeek:
        newString = line.split()
        # get the the date of the last class in next week
        nextShit = next_weekday(datetime.today(), int(newString[0]))
        # stripe it into %Y%m%d form
        # String nextDay;
        nextDay = nextShit.strftime('%Y%m%d')
        # String parseTime;
        parseTime = datetime.strptime(nextDay, "%Y%m%d")
        catDay = str(nextDay) + newString[1]
        reDay = re.sub("[^0-9]", "", catDay)

        assignment[reDay] = newString[2]
    # end for

    # sort the dictionary by date and time
    sortDict(assignment)

    # delete expired assignments
    # key is the date
    loopIndice = 0.07
    for key in list(assignment):
        stringDate = key[:8]      # take out YMD only
        copy = assignment[key]
        if int(stringDate) < todayDate:     # if the date is less than today's date
            del assignment[key]            # the assignment has passed due date

        #### Print out message of deletion of past events ###
            pastLabel = Label(bigFrame, text = (copy + " is automatically deleted because it is in the past now."), background="red", font = ("osaka", 18))
            pastLabel.grid()
            loopIndice += 0.04
            pastLabel.place(relx = 0.17, rely = loopIndice)

        #####################################################

        # end if
    # end for
# end

if os.stat("DataBase.db").st_size != 0:
    sortDict(assignment)
requestLabel = Label(bigFrame, text = "This box is for direct command operations", font = ("times", 18))
requestLabel.grid()
cmdBox = loopIndice + 0.08
requestLabel.place(relx = 0.35, rely = cmdBox)

cmdOpenField = Entry(bigFrame, width = 37)
cmdOpenField.grid()
cmdOpenField.place(relx = 0.33, rely = cmdBox+0.05)


################### BACKEND CODE ENDS HERE ####################

indQuizOpenField = Entry(bigFrame, width = 15)
indQuizOpenField.grid()
indQuizOpenField.place(relx = 0.43, rely = 0.9)

Welcome = Label(bigFrame, text = "Welcome to Todo App Developed by James Li", font = ("avenir", 16))
Welcome.grid()
Welcome.place(relx = 0.33, rely = 0.01)

todayLabel = Label(bigFrame, text=("Today is " + datetime.today().strftime('%Y-%m-%d') + "."), font=("avenir", 16))
todayLabel.grid()
todayLabel.place(relx=0.43, rely=0.04)

thanksLabel = Label(bigFrame, text="Thanks for using this app. Have a nice one :)", font=("avenir", 16))
thanksLabel.grid()
thanksLabel.place(relx=0.35, rely=0.07)

indQuizButton = Button(bigFrame, text = "Open Ind Quiz", style="TButton", command = longestName(assignment))
indQuizButton.grid()
indQuizButton.place(relx = 0.42, rely = 0.6)

root.mainloop()
