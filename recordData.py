from time import sleep
import RPi.GPIO as GPIO
import random

print("inside of recordData.py")

fileToPrint = "testRecordData.txt"

adcIn = 12
#pulses
pSignal = 15
pSH = 18
pADC = 17

low = GPIO.LOW
high = GPIO.HIGH

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(pSignal, GPIO.OUT)
GPIO.setup(pSH, GPIO.OUT)
GPIO.setup(pADC, GPIO.OUT)
GPIO.output(pSignal, low)
GPIO.output(pSH, low)
GPIO.output(pADC, low)

GPIO.setup(adcIn, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)

CurrentPointData = []
MaxPointData = []
PointData = []

pointsToTake = 50
pointsToAverage = 5

print("START")

#turn on ADC and sleep 1 ms for adc to be on
GPIO.output(pADC, GPIO.HIGH)
sleep(.001)

data = 3
dat = 2
da = 1

#multiply the ranges to get the depth/row count 3*10 = 30
for i in range(3):
    
    #Turn on Signal and Sample+Hold at the same time
    pass_list = (pADC, pSignal)
    GPIO.output(pass_list, high)

    for i in range(pointsToTake):
        
        #collect data points * 10
        data = random.randint(0,100)  #GPIO.input
        dat = random.randint(0,50) * 2
        da = random.randint(0,25) * 4
        #store in CurrentPointData
        data += 1
        dat +=1
        da +=1
        CurrentPointData.append([data, dat, da])
        #print(CurrentPointData)

    #PointData.append(CurrentPointData)
    #print(PointData)
    #print("SHOULD BE ABOVE")
    #del CurrentPointData[:30]
    #print(PointData)
    #print("SHOULD BE ABOVE")
    #del CurrentPointData[:]
PointData.append(CurrentPointData)

#number = random.randint(0,10)

#for i in range(3):
   # print i
   # for j in range(10):
   #     for k in range(1,3,1):
  #          
 #           CurrentPointData.append(number + k)
#
 #   PointData.append(CurrentPointData)
    
#print("Printing Points")
#print(PointData)

#for i in PointData:
#    print("h -"),
#    print(len(i)),
#    print(i)
#    for j in i:
        #print("IN J"),
        #print j
#        nothing = 0


#find max value in each subset of PointData
for i in PointData:
    for j in i:
        maxV = -9999
        for k in j:
            if(k>maxV):
                maxV = k
        MaxPointData.append(maxV)
        maxV=0

print("PrintingMax") #Prints Max points of Data
#print(MaxPointData)
#for i in MaxPointData:
#    print(i)

print(MaxPointData)
print(len(MaxPointData))

#make it nicer to see, split into different rows? or different arrays.

r1 = MaxPointData[:pointsToTake]
del MaxPointData[:pointsToTake]
#print(r1)
r2 = MaxPointData[:pointsToTake]
#print(r2)
del MaxPointData[:pointsToTake]
r3 = MaxPointData[:pointsToTake]
#print(r3)

print("R1 - "),
print(len(r1))
print(r1)
print("R2 - "),
print(len(r2))
print(r2)
print("R3 - "),
print(len(r3))
print(r3)

AvgVerticalData = []
#Average Vertically
for i in range(pointsToTake): #length of r arrays
    summ = 0
    summ = r1[i] + r2[i] + r3[i]
    avg = summ/3 # number of points taken to reaverage vertically. match with r arrays

    AvgVerticalData.append(avg)

print("After Vertical Average")
print(AvgVerticalData)
print(len(AvgVerticalData))
arLength = len(AvgVerticalData)
AvgHorData = []
skip = False
indexCounter = 0 #range to average number
for i in range(pointsToTake): # length of r arrays

    if(skip):
        #do nothing until leave loop
        nothing = 0

    else:            
        summ = 0
        for j in range(pointsToAverage): #range to average
            #print("COUNTERADDS = "),
            #print(indexCounter + j)
            summ += AvgVerticalData[indexCounter+j]
            #print("ADDED"),
            #print(AvgVerticalData[indexCounter+j])
        avg = summ/pointsToAverage # range to average
        #print("STORING VALUE = "),
        #print(avg)
        AvgHorData.append(avg)
        indexCounter+=pointsToAverage
        if(indexCounter>=arLength):
            skip = True

print("After Horizontal Avg")
print(AvgHorData)

print("This would be data to put into A scan")
print("(Put this into FinalFileOpen")
print(AvgHorData)

f = open(fileToPrint, "a+")

for i in AvgHorData:
    f.write(str(i))
    f.write(" ")
f.write("\n")
f.close()

GPIO.cleanup()
