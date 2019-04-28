from tkinter import *
from tkinter.ttk import *
import sys

def quit():
    sys.exit()

g = Tk()
g.title('Gui')

lbl = Label(g, text="press to quit.")
lbl.pack()
btn = Button(g, text="Quit", style="TButton", command=quit)
btn.pack()

g.mainloop()
