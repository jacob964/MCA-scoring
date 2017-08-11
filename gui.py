from tkinter import *

from tkinter import ttk

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("MCA image scoring")
        

        # Epithelial radio button
        epithelialFrame = ttk.Frame(master, padding=10)
        epithelialFrame.grid(column=0,row=0,sticky=(N,W))
        
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
        mesenchymalFrame.grid(column=0,row=1,sticky=(N,W))

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

        
        
root = Tk()
my_gui = GUI(root)
root.mainloop()