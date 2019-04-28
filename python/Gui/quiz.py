from tkinter import *
from tkinter.ttk import *
import webbrowser

# Analysis by James: webbrowser is indispensable for opening a website using python
def openRenauQuiz():
    site = "https://users.soe.ucsc.edu/~renau/ce110"
    webbrowser.open(site)

def openCS112IndQuiz():
    indQuiz = str(indQuizOpenField.get())
    site1 = "http://tiny.cc/cmps112-" + indQuiz + "-ind"
    webbrowser.open(site1)

def openCS112GrpQuiz():
    grpQuiz = str(grpQuizOpenField.get())
    site2 = "http://tiny.cc/cmps112-" + grpQuiz + "-grp"
    webbrowser.open(site2)



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

renauQuizButton = Button(bigFrame, text = "Open CE110 Quiz", command = openRenauQuiz)
renauQuizButton.grid()
renauQuizButton.place(relx = 0.4, rely = 0.8)

root.mainloop()
