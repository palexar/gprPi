import sys
import os
import serial
import time
from collections import Counter
from Tkinter import*
import Tkinter
import tkSimpleDialog
#import Tkinter
import tkMessageBox
import RPi.GPIO as GPIO

unoBat = 16 #pin to output from

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(unoBat, GPIO.OUT)
GPIO.output(unoBat, 1)
time.sleep(1)
vList = []
for i in range(10):

    #element = 10
    ser = serial.Serial('/dev/ttyACM0', 2000000)
    read_serial=ser.readline()
    #print(read_serial)
    element = read_serial[:-2]
    print(element)
    el = float(element)
    actualEl = el-0.03
    actualVolt = actualEl * 4.313
    vList.append(actualVolt)
    print(actualVolt)
    #time.sleep(.1)

cnt = Counter(vList)
GPIO.output(unoBat,0)
print("MOST COMMON VOLTAGE")
print(cnt.most_common(1))
te = cnt.most_common(1)
batV = te[0][0]
print(cnt[0])
print("te : "),
print(te[0][0])
print("batV = "),
print(batV)


#w = Label(tk, text="my Program")
#w.pack()

root = Tk()
root.geometry('550x200')
displayString = "Battery is at: "
print(int(batV*100))
print(float(int(batV*100))/100.00)
fa = int(batV*100)
disBatV = float(fa)/100.00
displayString+=str(disBatV)
displayString+= " V."
tkMessageBox.showinfo("Battery Voltage", displayString)

root.update()
root.destroy()




