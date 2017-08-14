from tkinter import *
from tkinter import ttk

from time import strftime, localtime
import os

class GUI:
    def __init__(self, master):
        self.undoFlag = 0
        self.makeGUI(master)
        
    def makeGUI(self, master):   
        self.master = master
        master.title("MCA image scoring")

        # Sample condition entry boxes
        sampleFrame = ttk.Frame(master, padding=10)
        sampleFrame.grid(column=0, row=0, sticky=(N,W))
        
        self.exptName = StringVar()
        exptName = self.exptName
        self.condition = StringVar()
        condition = self.condition
        self.supplement = StringVar()
        supplement = self.supplement
        self.day = StringVar()
        day = self.day

        ttk.Label(sampleFrame, text="Experiment Name:     ").grid(row=0, column=0, sticky=W)
        ttk.Entry(sampleFrame, width=30, textvariable=exptName).grid(row=0, column=1, stick=W)        
        ttk.Label(sampleFrame, text=" ").grid(row=1, column=0)
        ttk.Label(sampleFrame, text="Condition Name:      ").grid(row=2, column=0, sticky=W)
        ttk.Entry(sampleFrame, width=30, textvariable=condition).grid(row=2, column=1, stick=W)
        ttk.Label(sampleFrame, text=" ").grid(row=3, column=0)
        ttk.Label(sampleFrame, text="Supplement:      ").grid(row=4, column=0, sticky=W)
        ttk.Entry(sampleFrame, width=30, textvariable=supplement).grid(row=4, column=1, stick=W)        
        ttk.Label(sampleFrame, text=" ").grid(row=5, column=0)
        ttk.Label(sampleFrame, text="Day:      ").grid(row=6, column=0, sticky=W)
        ttk.Entry(sampleFrame, width=30, textvariable=day).grid(row=6, column=1, stick=W)        
               
        
        
        # Epithelial radio button
        epithelialFrame = ttk.Frame(master, padding=10)
        epithelialFrame.grid(column=0,row=1,sticky=(N,W))
        
        self.epithelial  = IntVar()       # epithelial rating
        epithelial = self.epithelial

        ttk.Label(epithelialFrame, text="Epithelial score            ").grid(row=0, column=0, sticky=W)
        
        ttk.Radiobutton(epithelialFrame, text="  ", variable=epithelial, value=0).grid(row=0, column=1)
        ttk.Radiobutton(epithelialFrame, text="  ", variable=epithelial, value=1).grid(row=0, column=2)
        ttk.Radiobutton(epithelialFrame, text="  ", variable=epithelial, value=2).grid(row=0, column=3)
        ttk.Radiobutton(epithelialFrame, text="  ", variable=epithelial, value=3).grid(row=0, column=4)

        ttk.Label(epithelialFrame, text = " 0").grid(row=1, column=1, sticky=W)
        ttk.Label(epithelialFrame, text = " 1").grid(row=1, column=2, sticky=W)
        ttk.Label(epithelialFrame, text = " 2").grid(row=1, column=3, sticky=W)
        ttk.Label(epithelialFrame, text = " 3").grid(row=1, column=4, sticky=W)
        
        
        # Mesenchymal radio button
        mesenchymalFrame = ttk.Frame(master, padding=10)
        mesenchymalFrame.grid(column=0,row=2,sticky=(N,W))

        self.mesenchymal  = IntVar()       # epithelial rating
        mesenchymal = self.mesenchymal
        
        ttk.Label(mesenchymalFrame, text="Mesenchymal score   ").grid(row=0, column=0, sticky=W)
  
        ttk.Radiobutton(mesenchymalFrame, text="  ", variable=mesenchymal, value=0).grid(row=0, column=1)
        ttk.Radiobutton(mesenchymalFrame, text="  ", variable=mesenchymal, value=1).grid(row=0, column=2)
        ttk.Radiobutton(mesenchymalFrame, text="  ", variable=mesenchymal, value=2).grid(row=0, column=3)
        ttk.Radiobutton(mesenchymalFrame, text="  ", variable=mesenchymal, value=3).grid(row=0, column=4)
        
        ttk.Label(mesenchymalFrame, text = " 0").grid(row=1, column=1, sticky=W)
        ttk.Label(mesenchymalFrame, text = " 1").grid(row=1, column=2, sticky=W)
        ttk.Label(mesenchymalFrame, text = " 2").grid(row=1, column=3, sticky=W)        
        ttk.Label(mesenchymalFrame, text = " 3").grid(row=1, column=4, sticky=W)

        
        
        # Buttons
        buttonFrame = ttk.Frame(master, padding=10)
        buttonFrame.grid(column=1, row=4, sticky=E)
        ttk.Button(buttonFrame, text="Undo", command=self.undoEntry).grid(column=0, row=0, sticky=E)
        ttk.Button(buttonFrame, text="Add data", command=self.logData).grid(column=1, row=0, sticky=E)
        
        
    def undoEntry(self):
        if self.undoFlag == 0:
            fileName = self.undoTempFname
            file = open(fileName, "r+", encoding = "utf-8")

            #Move the pointer (similar to a cursor in a text editor) to the end of the file. 
            file.seek(0, os.SEEK_END)

            #This code means the following code skips the very last character in the file - 
            #i.e. in the case the last line is null we delete the last line 
            #and the penultimate one
            pos = file.tell() - 2

            #Read each character in the file one at a time from the penultimate 
            #character going backwards, searching for a newline character
            #If we find a new line, exit the search
            while pos > 0 and file.read(1) != "\n":
                pos -= 1
                file.seek(pos, os.SEEK_SET)

            #So long as we're not at the start of the file, delete all the characters ahead of this position
            if pos > 0:
                pos += 1
                file.seek(pos, os.SEEK_SET)
                file.truncate()

            file.close()
            self.undoFlag = 1
        else:
            return
        
    def logData(self):
        fileName = str(self.exptName.get()) + ".csv"
        
        if os.path.isfile(fileName) == False:
            f = open(fileName, 'w')
            f.writelines("Condition, Supplement, Day, Epithlial, Mesenchymal\n")
        else:
            f = open(fileName, 'a')
        
        f.writelines( str(self.condition.get()) + "," )
        f.writelines( str(self.supplement.get()) + "," )
        f.writelines( str(self.day.get()) + "," )
        f.writelines( str(self.epithelial.get()) + "," )
        f.writelines( str(self.mesenchymal.get()) + "\n" )
        f.close()

        self.undoTempFname = fileName
        self.undoFlag = 0
        
        
    def dateName(self):
        dateStr = strftime("%Y-%B-%d", localtime())
        return dateStr
        
        
    def timeName(self):
        timeStr = strftime("%I-%M-%S %p", localtime())
        return timeStr

        
        
root = Tk()
my_gui = GUI(root)
root.mainloop()