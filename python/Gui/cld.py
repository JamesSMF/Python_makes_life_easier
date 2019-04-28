from tkinter import *
from tkinter.ttk import *
import re
import os
from collections import OrderedDict
from datetime import datetime, date, time, timedelta

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

assignment = dict()   # restructured: map from due dates to assignment


#GUI CODE:

root = Tk()
root.geometry("500x500")
# root.resizeable(0,0)

# analysis by James: This initializes the app frame size.
bigFrame = Frame(root, width = 495, height = 495, relief = "raise")
bigFrame.grid()
bigFrame.place


indQuizOpenField = Entry(bigFrame, width = 15)
indQuizOpenField.grid()
indQuizOpenField.place(relx = 0.4, rely = 0.2)

indQuizLabel = Label(bigFrame, text = "Enter Ind Quiz Name:", font = ("helvetica", 10))
indQuizLabel.grid()
indQuizLabel.place(relx = 0.4, rely = 0.1)

indQuizButton = Button(bigFrame, text = "Open Ind Quiz", style="TButton", command = openCS112IndQuiz)
indQuizButton.grid()
indQuizButton.place(relx = 0.42, rely = 0.3)

###############################################################################################################

# Analysis by James: Entry is for user input, and it takes two paras: (frame, width)
grpQuizOpenField = Entry(bigFrame, width = 15)
grpQuizOpenField.grid()

# Analysis by James: relx and rely are the coordinate of the entry box
grpQuizOpenField.place(relx = 0.4, rely = 0.5)

grpQuizLabel = Label(bigFrame, text = "Enter Grp Quiz Name:", font = ("helvetica", 10))
grpQuizLabel.grid()
grpQuizLabel.place(relx = 0.4, rely = 0.4)

grpQuizButton = Button(bigFrame, text = "Open Grp Quiz", style="TButton", command = openCS112GrpQuiz)
grpQuizButton.grid()
grpQuizButton.place(relx = 0.42, rely = 0.6)

###############################################################################################################
root.mainloop()
