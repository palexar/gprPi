import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from Tkinter import *
import tkSimpleDialog
import tkMessageBox

fileNamed = "testRecordData.txt"
# use scanTestD.txt for actual data
# use testRecordData.txt for random data

depthFactor = 1 # this is the depth at which each point is taken
print("INSIDE OF A")

def getData(number):
        
    listDat =[]
    counter = 0
    f = open(fileNamed, "r")
    if f.mode == "r":
            contents = f.readlines()
            contents = [x.strip() for x in contents]
            listDat.append(contents)
            counter+=1
    #print(listDat)
    #for i in listDat[0]:
        #for j in i:
            #print(":"),
            #print(j),
            #print(":")

    datList= listDat[0]

    digitToAdd=""
    actualData = []
    for i in datList[number]:
        #print(i)
        if(i==' '):
            actualData.append(digitToAdd)
            digitToAdd=""
        else:
            digitToAdd+=i

    #print(actualData)
    #for i in actualData:
        #p#rint i

    return actualData 

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


root = Tk()
root.geometry('550x200')
w = Label(root, text="my Program")
w.pack()

counter = 0
listData = []
a = open(fileNamed, "r")
if a.mode == "r":
    contents = a.readlines()
    contents = [x.strip() for x in contents]
    listData.append(contents)
    counter+=1
    #print(listData)
    #print(len(listData[0]))

scanNum = tkSimpleDialog.askinteger("scan #", "please enter Scan #1-" + str(len(listData[0])) )
scanNum-=1
scanData = getData(scanNum)
remover = scanData.pop()
newScaner = scanData
scanDara = newScaner
#print(scanData)
#print(scanData[-1])
root.destroy()
xDataTest = range(len(scanData))
#counter = 0
#for i in scanData:
#    if(float(i)<5.0):
#        print i
#        print("FOUND A ZERO")
#        print(counter)
#    counter+=1

xData = [x+depthFactor for x in xDataTest]
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.xlabel("Depth (meters)")
plt.ylabel("Strength of Wave Reflection")
plt.title("A Scan")
plt.plot(xData, scanData, 'b')

plt.show()
