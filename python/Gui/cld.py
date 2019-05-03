from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import re
import os
from collections import OrderedDict
from datetime import datetime, date, time, timedelta

################### FUNCTIONS #####################

# translate human readable rgb to tkinter syntax
# inputs a tuple of three ints
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

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

# input: a string      output: a formated string
def dateFormat(dateStr):
    dateList=list()
    for i in range(4):    # stores year
        dateList.append(dateStr[i])
    dateList.append('-')
    for i in range(4, 6):  # stores month
        dateList.append(dateStr[i])
    dateList.append('-')
    for i in range(6, 8):  # stores day
        dateList.append(dateStr[i])
    dateList.append('  ')
    for i in range(8, 10): # stores hour
        dateList.append(dateStr[i])
    dateList.append(' : ')
    for i in range(10, 12): # stores minute
        dateList.append(dateStr[i])

    return "".join(dateList)

# This function saves the process to DataBase.db
def saveProcess():
    with open("DataBase.db", "w") as f:
        for key in assignment:
            f.write(key+' '+str(assignment[key])+'\n')
        # end for
    # end with

# This function is used for return message
# which is right below the input box
def return_message(message):
    tempLabel = tk.Label(bigFrame, text = message, font = ("avenir", 16), fg=_from_rgb((100,105,80)), bg=_from_rgb((231,231,231)))
    tempLabel.grid()
    tempLabel.place(relx = 0.33, rely = 0.5)



# This functions updates the list
def listEvents(prevLineNum):
    # save the process first ---------------------
    saveProcess()

    if len(assignment) == 0:     # there is nothing in the dict()
        noEventLabel = Label(bigFrame, text = "Your to-do list is empty.", font = ("avenir", 16))
        noEventLabel.grid()
        noEventLabel.place(relx = 0.25, rely = prevLineNum)
        return
    else:
        longest = longestName(assignment)  # get the length of longest key
        count = 0     # limit to 16 print-outs
        for key in assignment:
            keylen = len(assignment[key])
            diff = longest - keylen + 2
            count += 1
            if count == 17:
                break

            todayYear=list()
            currYear=list()
            todayMon=list()
            currMon=list()
            todayDay=list()
            currDay=list()
            for i in range(8):
                if i<4:
                    todayYear.append(str(todayDate)[i])
                    currYear.append(key[i])
                elif i<6:
                    todayMon.append(str(todayDate)[i])
                    currMon.append(key[i])
                else:
                    todayDay.append(str(todayDate)[i])
                    currDay.append(key[i])
            # end for

            fuckCurrYear = "".join(currYear)
            fuckTodayYear = "".join(todayYear)
            fuckCurrMon = "".join(currMon)
            fuckTodayMon = "".join(todayMon)
            fuckCurrDay = "".join(currDay)
            fuckTodayDay = "".join(todayDay)

            delta = date(int(fuckCurrYear), int(fuckCurrMon), int(fuckCurrDay)) - date(int(fuckTodayYear), int(fuckTodayMon), int(fuckTodayDay))
            difference = int(delta.days)

            # create a set of event names in weekly calendar
            nextWeek = open("Weekly.db", "r")
            listWeek = set()
            for ddd in nextWeek:
                listWeek.add(ddd.split()[2])
            nextWeek.close()

            weekdayCode = datetime.strptime(key, "%Y%m%d%H%M").weekday()
            wdaydict = {0:'Mon ',1:'Tues',2:'Wed ',3:'Thur',4:'Fri ',5:'Sat ',6:'Sun '}
            if difference == 1:
                listTomorrowLabel = tk.Label(bigFrame, text = (assignment[key] + diff * " " + str(dateFormat(key), ) + ' ' + wdaydict[weekdayCode] + " (tomorrow)"), fg=_from_rgb((97,97,183)), bg=_from_rgb((231,231,231)), font = ("menlo", 16))
                listTomorrowLabel.grid()
                listTomorrowLabel.place(relx = 0.1, rely = prevLineNum)
            elif difference == 0:
                listTodayLabel = tk.Label(bigFrame, text = (assignment[key] + diff * " " + str(dateFormat(key), ) + ' ' + wdaydict[weekdayCode] + " (today)"), fg=_from_rgb((97,97,183)), bg=_from_rgb((231,231,231)), font = ("menlo", 16))
                listTodayLabel.grid()
                listTodayLabel.place(relx = 0.1, rely = prevLineNum)
            else:
                listRdayLabel = tk.Label(bigFrame, text = (assignment[key] + diff * " " + str(dateFormat(key), ) + ' ' + wdaydict[weekdayCode] + " (in " + str(difference, ) + " days)"), bg=_from_rgb((231,231,231)), font = ("menlo", 16))
                listRdayLabel.grid()
                listRdayLabel.place(relx = 0.1, rely = prevLineNum)
            # end if-else
            prevLineNum += 0.03
        # end for
    # end if(lenght==0)
# end of list function

# This function takes an input of a text array
# It maps a time to an event
def mapFunc():
    charArray[-1] = re.sub("[^0-9]", "", charArray[-1])
    if len(charArray[-1])==1:
        if int(charArray[-1][0]<6):
            charArray[-1]=str(int(charArray[-1])+1200)
        else:
            charArray[-1] = str('0' + charArray[-1])

    if len(charArray[-1])!=4:
        errorLabel = tk.Label(bigFrame, text = "Please enter a valid time.", font=("Arial", 16))

    if charArray[-1]=='today' or charArray[-1]=='tonight':
        Date = datetime.today().strftime("%Y%m%d")
        Date = Date+str(charArray[-1])
    elif charArray[-2]=='tomorrow':
        Date = str(date.today() + timedelta(days=1))
        Date = Date + str(charArray[-1])
    elif charArray[-2]=="Sun" or charArray[2]=="Sunday":
        # String nextDate;
        nextDate = next_weekday(datetime.today(), 6).strftime('%Y%m%d')
        Date = nextDate + str(charArray[-1])
    elif charArray[-2]=="Mon" or charArray[2]=="Monday":
        nextDate = next_weekday(datetime.today(), 0).strftime("%Y%m%d")
        Date = nextDate + str(charArray[-1])
    elif charArray[-2]=="Tues" or charArray[2]=="Tuesday":
        nextDate = next_weekday(datetime.today(), 1).strftime('%Y%m%d')
        Date = nextDate + str(charArray[-1])
    elif charArray[-2]=="Wed" or charArray[2]=="Wednesday":
        nextDate = next_weekday(datetime.today(), 2).strftime('%Y%m%d')
        Date = nextDate + str(charArray[-1])
    elif charArray[-2]=="Thurs" or charArray[2]=="Thursday":
        nextDate = next_weekday(datetime.today(), 3).strftime('%Y%m%d')
        Date = nextDate + str(charArray[-1])
    elif charArray[-2]=="Fri" or charArray[2]=="Friday":
        nextDate = next_weekday(datetime.today(), 4).strftime('%Y%m%d')
        Date = nextDate + str(charArray[-1])
    elif charArray[-2]=="Sat" or charArray=='Saturday':
        nextDate = next_weekday(datetime.today(), 5).strftime('%Y%m%d')
        Date = nextDate + str(charArray[-1])
    else:
        if(len(charArray[-1])==12):
            Date=charArray[-1]
        else:
            Date = "".join(charArray[-1:])
    # end if-else

    Date = re.sub("[^0-9]", "", Date)
    if len(Date)==4:
        Date = datetime.today().strftime("%Y%m%d") + Date
    if len(Date)!=12:
        print("Please enter a valid date.\n")

    # time conflict check
    if os.stat("DataBase.db").st_size != 0:
        flag = True
        for datE in assignment:
            targetTime = datetime.strptime(datE,"%Y%m%d%H%M") # datetime type
            compTime = datetime.strptime(Date,"%Y%m%d%H%M")   # datetime type
            diffTime = compTime - targetTime     # calculate the time difference
            if diffTime<timedelta(minutes=0):    # absolute value
                diffTime = - diffTime



################### GUI CODE #######################

root = Tk()
root.geometry("970x710")
# root.resizeable(0,0)

# analysis by James: This initializes the app frame size.
bigFrame = Frame(root, width = 970, height = 710, relief = "raise")
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

            pastLabel = Label(bigFrame, text = (copy + " is automatically deleted because it is in the past now."), background="red", font = ("osaka", 15))
            pastLabel.grid()
            loopIndice += 0.03
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
requestLabel.place(relx = 0.23, rely = cmdBox)

cmdOpenField = Entry(bigFrame, width = 37)
cmdOpenField.grid()
boxCoord = cmdBox+0.05
cmdOpenField.place(relx = 0.22, rely = boxCoord)


################### BACKEND CODE ENDS HERE ####################

Welcome = tk.Label(bigFrame, text = "Welcome to Todo App Developed by James Li", font = ("avenir", 16), fg=_from_rgb((200,145,150)), bg=_from_rgb((231,231,231)))
Welcome.grid()
Welcome.place(relx = 0.33, rely = 0)

todayLabel = tk.Label(bigFrame, text=("Today is " + datetime.today().strftime('%Y-%m-%d') + "."), font=("avenir", 16), fg=_from_rgb((200,145,150)), bg=_from_rgb((231,231,231)))
todayLabel.grid()
todayLabel.place(relx=0.43, rely=0.04)

thanksLabel = tk.Label(bigFrame, text="Thanks for using this app. Have a nice one :)", font=("avenir", 16), fg=_from_rgb((200,145,150)), bg=_from_rgb((231,231,231)))
thanksLabel.grid()
thanksLabel.place(relx=0.35, rely=0.07)

listButton = Button(bigFrame, text = "update event list", style="TButton", command = listEvents(0.2+boxCoord))
listButton.grid()
listButton.place(relx = 0.6, rely = cmdBox)

root.mainloop()
