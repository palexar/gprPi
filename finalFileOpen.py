import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

debugMode = False

#CONSTANTS FOR GRAPH
yaxisTicksPerRead = 0.3
readingsDeep = 0 # to be calculated after reading data. max depth scanned/read

blueStartZone = 0
greenStartZone = 3
redStartZone = 6
redEndZone = 10

listDat = []
counter = 0

f = open("scanDat.txt", "r")
if f.mode == "r":
        contents = f.readlines()
        contents = [x.strip() for x in contents]
        listDat.append(contents)
        counter+=1
        #print(contents)
# MARK UNCOMMENTS ------------------------------------
l = listDat[0][0]
p = l.split()
#print l.split()
#print p[0]
#print len(p)
#print(listDat)
datList = listDat[0]

count = 0
for i in datList[0]:
        for elem in i:
                #print (elem)
                count+=1
#print("COUNTER = "),
#print(count)
#print("Divide by 2"),
#print(count/2)

arrayLength = count/2

testFlip = [[] for i in range(arrayLength+1)]
#print(testFlip)
cou = 0
for j in datList:
        for elem in j:
                if(elem==' '):
                        pass
                else:
                        testFlip[cou].append(elem)
                        cou+=1
                if(cou>=arrayLength+1):
                        cou=0

#for i in testFlip:
#        print i
# MARK UNCOMMENTS ------------------------------------
if(debugMode):        
        print("PRINTING ORIGINAL")
        for j in datList:
            for elem in j:
                if(elem==' '):
                    pass
                else:
                    print(elem),
            print("\n")

# MARK UNCOMMENTS ------------------------------------   
if(debugMode):
        print("PRINTING FLIPPED")


        for j in testFlip:
            for elem in j:
                print(elem),
            print("\n")

#x values should be meters

# MARK UNCOMMENTS ------------------------------------   
#print("TESTING ROW DEPTH")
#print(len(testFlip))

readingsDeep = -(len(testFlip) - 1)*yaxisTicksPerRead

#y values will be depth
y = testFlip

# MARK UNCOMMENTS ------------------------------------
#print(len(y[0])) #prints columns

#for j in y:
#    yplot = np.arange(0.0, 5.0, 0.1)

# MARK UNCOMMENTS ------------------------------------
#print (len(testFlip)) # prints rows

# THIS IS THE MARK FOR DRAWING DATA AS
# DRAFTED ON PAPER

#Constants


#dont touch these ones
red = redStartZone
green = greenStartZone
blue = blueStartZone




#print("PRINTING rows and column counters")
#rows = 0
#columns = 0

#for i in testFlip:
#        print("R -"),
#        print(rows),
#        print("C -"),
#        for j in i:
#                print(columns),
#                columns+=1
#        columns = 0
#        rows+=1


# MARK UNCOMMENTS ------------------------------------
#print("MAKING NEW DATA ****")
NewArrayData = []
DrawingData = []
rows = 0
columns = 0
xStart = 0
xEnd = 1
for i in testFlip:
        for j in i:
               # print("LENGTH I = "),
               # print(len(i))
                
               # print("COLUMNS + 1 = "),
               # print(columns),
                #print(columns+1)
                if (columns+1>=len(i)):
                        #go to next row and flush data
                        #print("got here"),
                        #print(columns)
                        #print(j)
                        xEnd = columns
                        c = testFlip[rows][columns]
                        ccolor = "test"
                        if (int(c)<green):
                                #blue
                                #print("SHOULD BE BLUE")
                                ccolor = 'b'
                        else:
                                if(int(c)<red):
                                        #green
                                        ccolor = 'g'
                                else:
                                        #is red
                                        ccolor = 'r'
                        NewArrayData.append([xStart,xEnd+1,ccolor])
                else:
                        #check datas
                        check = testFlip[rows][columns+1]
                        c = testFlip[rows][columns]
                        chcolor = "test" #next Color to check
                        ccolor = "test" # Current Color to compare with
                        #print("C IS : "),
                        #print(c)
                        
                        #print("CH is : "),
                        #print(check)
                        if (int(check)<green):
                                #blue
                                chcolor = 'b'
                        else:
                                if(int(check)<red):
                                        #green
                                        chcolor = 'g'
                                else:
                                        #is red
                                        chcolor = 'r'
                        #print("CHECKING CURRENT COLOR VERSES OTHER STUFF")
                        #print(c),
                        #print(green),
                        #print(c<green)
                        #print("return as int")
                        #print(int(c)),
                        #print(green),
                        #print(int(c)<green)
                        if (int(c)<green):
                                #blue
                                #print("SHOULD BE BLUE")
                                ccolor = 'b'
                        else:
                                if(int(c)<red):
                                        #green
                                        ccolor = 'g'
                                else:
                                        #is red
                                        ccolor = 'r'
                        #print(ccolor)
                        #print(chcolor)
                        if(ccolor==chcolor):
                                #colors are same value range
                                xEnd+=1
                        else:
                                #colors are not same, flush data
                                #print("HERTTING HERE")
                                NewArrayData.append([xStart, xEnd, ccolor])
                                #NewArrayData.append([1,2,3])
                                #for x in NewArrayData:
                                #        print(x)
                                #        for y in x:
                                #                print(y)
                               # print(NewArrayData)
                                #if(testFlip[columns+100]):
                                #        crash = 0
                                xStart = xEnd
                                xEnd += 1
                        columns+=1
        #Next Row. Reset Counters flush data
        DrawingData.append(NewArrayData)
        NewArrayData = []
        columns = 0
        xStart = 0
        xEnd = 1
        rows+=1
        #print("END OF ROW_____________________________")

# MARK UNCOMMENTS ------------------------------------
#r = 0
#print("PRINTING Drawing DATA NOW")
#for i in DrawingData:
#        print("R"),
#        print(r),
#        print(i)
#        r+=1

# MARK UNCOMMENTS ------------------------------------
#print("Length of DrawingData")
#print(len(DrawingData))

# MARK UNCOMMENTS ------------------------------------
#print("Length of each row in DrawingData")
#for i in DrawingData:
#        print(len(i))
#        print(i)

# MARK UNCOMMENTS ------------------------------------
#print("TO ACCESS EACH VARIABLE IN DrawingData")
#print(DrawingData[8][0])
#print(DrawingData[8][1])

#for i in DrawingData:
        #for j in i:
                #print(j)
                #print("PRINTS SUBSET LIST VALUES")
                #print(DrawingData[3][0]) #TO ACCESS CERTAIN SUBSET VALUES
                #FOR EACH VAR VALUE IN EACH SUBSET LIST
                #for k in j:
                #        print(k)
yValue = 0
rows = 0
columns = 0
for row in DrawingData:
        for column in row:
                
                xaxis = np.linspace(int(column[0]),int(column[1]),10)
                
                yaxis = np.linspace(yValue,yValue,10)
                

                plt.plot(xaxis,yaxis,column[2], linewidth = 28.0)
                columns+=1
        yValue-=0.3
        rows+=1
        columns=0

#for i in testFlip:
#        print(counting),
#        counting += 1
#        print(i)

#CHANGE XTEST TO BE THE LENGHT OF DATA/ COLUMNS
#xtest = np.linspace(0, 9, 9)
#ytest = y[3]
#z = y[3]
cmap = ListedColormap(['b', 'g', 'r'])
norm = BoundaryNorm([blueStartZone, greenStartZone, redStartZone, redEndZone], cmap.N)

#points = np.array([x,]).T.reshape(-1,1,2)
#segments = np.concatenate([points[:-1], points[1:]], axis=1)

#lc = LineCollection(segments, cmap=cmap, norm=norm)
#lc.set_array(z)
#lc.set_linewidth(3)

#plt.figure(1)
#fig1 = plt.figure()
#plt.gca().add_collection(lc)

#plt.xlim(0, 10)
#plt.ylim(-1, 10)

for r in DrawingData:
        nothing = 0

#WORKING CHUNK
x = np.arange(0.0, 5.0, 0.1)
ys = np.linspace(0, 0, 50)
yf = np.linspace(4,4,50)
        
#plt.plot(x, ys, 'b')
#plt.plot(x, yf, 'r')

#plt.plot(xtest, ytest, 'g')
#print(readingsDeep)
#print(yaxisTicksPerRead)
#linepa = np.arange(readingsDeep, yaxisTicksPerRead, yaxisTicksPerRead)
#print(linepa)
plt.yticks(np.arange(readingsDeep, yaxisTicksPerRead, yaxisTicksPerRead))
plt.show()




#plt.figure(1)
#plt.plot(x, y, 'b')

#plt.show()
