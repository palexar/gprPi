import sys
import os
import serial
import time
from Tkinter import *

window = Tk()

window.title("Running Python Script")
window.geometry('550x200')

#ser = serial.Serial('/dev/ttyACM0', 2000000)
#read_serial=ser.readline()
#element = read_serial[:-2]
#print(element)

def run():
    print("here")
    os.system('python ToHandleDigits.py')
    
def runA():
    print("hereA")
    os.system('python AscanSetDepth.py')

def cle():
    print("del file records")
    os.remove("scanTestD.txt")

def scan():
    #Scan Arduino inputs
    print("Scanning and storing data to file")
    #os.system('python recordData.py') # for random number testing
    os.system('python Uno.py') # for actual Uno data
    print("Done")

def batCheck():
    print("Checking Batter")
    os.system('python checkBattery.py')
    print("dislplaying voltage")

btn = Button(window, text="Display B scan", bg="black", fg="white", command=run)
btn.grid(column=0, row=0)

btn = Button(window, text="Display A scan", bg="black", fg="white", command=runA)
btn.grid(column=1, row=0)

btn = Button(window, text="Clear Data File", bg="black", fg="white", command=cle)
btn.grid(column=2, row=0)

btn = Button(window, text="Scan Location", bg="black", fg="white", command=scan)
btn.grid(column=0, row=1)

btn = Button(window, text="Battery Check", bg="black", fg="white", command=batCheck)
btn.grid(column=3, row=0)
print("HERE")

window.mainloop()
