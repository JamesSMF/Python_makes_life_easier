import sys
from tkinter import *

class Example4:
    def __init__(self, master):
        # showInfo needs to know the master self.master = master
        # Create a frame to hold the widgets
        frame = Frame(master)
        # Create a Label to display a header self.headLbl = Label(frame, text="Widget Demo Program", relief=RIDGE) self.headLbl.pack(side=TOP, fill=X)
        # Create a border using a dummy frame with a large border width
        spacerFrame = Frame(frame, borderwidth=10)
        # Create another frame to hold the center part of the form
        centerFrame = Frame(spacerFrame)
        leftColumn = Frame(centerFrame, relief=GROOVE, borderwidth=2)
        rightColumn = Frame(centerFrame, relief=GROOVE, borderwidth=2)
        # Create some colorful widgets
        self.colorLabel = Label(rightColumn, text="Select a color")
        self.colorLabel.pack(expand=YES, fill=X)
        entryText = StringVar(master)
        entryText.set("Select a color")
        self.colorEntry = Entry(rightColumn, textvariable=entryText)
        self.colorEntry.pack(expand=YES, fill=X)
        # Create some Radiobuttons
        self.radioBtns = []
        self.radioVal = StringVar(master)
        btnList = ("black", "red", "green", "blue", "white", "yellow")
        for color in btnList:
            self.radioBtns.append(Radiobutton(leftColumn, text=color, value=color, indicatoron=TRUE,variable=self.radioVal, command=self.updateColor))
        else:
            if (len(btnList) > 0):
                self.radioVal.set(btnList[0])
                self.updateColor()
                for btn in self.radioBtns:
                    btn.pack(anchor=W)

                # Make the frames visible
                leftColumn.pack(side=LEFT, expand=YES, fill=Y)
                rightColumn.pack(side=LEFT, expand=YES, fill=BOTH)
                centerFrame.pack(side=TOP, expand=YES, fill=BOTH)
                # Create the Indicator Checkbutton
                self.indicVal = BooleanVar(master)
                self.indicVal.set(TRUE)
                self.updateIndic()
                Checkbutton(spacerFrame, text="Show Indicator", command=self.updateIndic,variable=self.indicVal).pack(side=TOP, fill=X)
                # Create the Color Preview Checkbutton
                self.colorprevVal = BooleanVar(master)
                self.colorprevVal.set(FALSE)
                self.updateColorPrev()
                Checkbutton(spacerFrame, text="ColorPreview", command=self.updateColorPrev,variable=self.colorprevVal).pack(side=TOP, fill=X)
                Button(spacerFrame, text="Info", command=self.showInfo).pack(side=TOP, fill=X) # Create the Quit Button
                Button(spacerFrame, text="Quit!", command=self.quit).pack(side=TOP, fill=X)
                spacerFrame.pack(side=TOP, expand=YES, fill=BOTH)
                frame.pack(expand=YES, fill=BOTH)

    def quit(self):
        sys.exit()

    def updateColor(self):
        self.colorLabel.configure(fg=self.radioVal.get())
        self.colorEntry.configure(fg=self.radioVal.get())

    def updateIndic(self):
        for btn in self.radioBtns:
            btn.configure(indicatoron=self.indicVal.get())



    def updateColorPrev(self):
        if (self.colorprevVal.get()):
            for btn in self.radioBtns:
                color = btn.cget("text")
                btn.configure(fg=color)
            else:
                for btn in self.radioBtns:
                    btn.configure(fg="black")


    def showInfo(self):
        toplevel = Toplevel(self.master, bg="white")
        toplevel.transient(self.master)
        toplevel.title("Program info")
        Label(toplevel, text="A simple Tkinter demo", fg="navy", bg="white").pack(pady=20)
        Label(toplevel, text="Written by Bruno Dufour", bg="white").pack()
        Label(toplevel, text="http://www.iro.umontreal.ca/~dufour/", bg="white").pack()
        Button(toplevel, text="Close", command=toplevel.withdraw).pack(pady=30)

def main():
    root = Tk()
    ex4 = Example4(root)
    root.title("A simple widget demo")
    root.mainloop()

main()
