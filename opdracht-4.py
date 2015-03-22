###############################################################################
##Afvinkopdracht 3, Blok 3, Richard Jansen HAN University Of Applied Sciences##
##17-03-2015###################################################################
###############################################################################

from tkinter import *
from tkinter import filedialog
niets=Tk()
file = filedialog.askopenfile()
niets.destroy()
niets.mainloop()

def main():
    x = startread(file)
    checkaa(x)
   
def startread(seq):
    raw_data = ""
    startReading = False
    for regel in seq:
        if startReading:
            raw_data += regel[10:]
        if ">" in regel:
            startReading = True
    sequence = raw_data.replace(' ','').replace('\n','').replace('\r','')
    print (sequence)    
    return sequence

def checkaa(x):
    seq = x.upper()
    if "B" in seq:
        print ('character B found in sequence, likely not a proteinsequence')
    else:
        print ('\nall characters are possibly amino-acids')

main()