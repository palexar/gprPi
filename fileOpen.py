import numpy as np

# DON'T STORE SPACES IN WITH DATA!!!!
listDat = []
counter = 0

f = open("scanDat.txt", "r")
if f.mode == "r":
        contents = f.readlines()
        contents = [x.strip() for x in contents]
        listDat.append(contents)
        counter+=1
        print(contents)

for j in listDat:
    for elem in j:
        print(elem),#, end=' ')

trDat = [[]]# for i in range




print("\n")
print counter
print listDat[0][1][2]
trDatCounter = 0

#for all in listDat:
#    print(all)
#    for row in all:
#        print(row)
#        for col in row:
#            print(col)
#            if(col == ' '):
#                print("BLANK")
#            else:
#                trDat[trDatCounter].append(col)
#        trDatCounter+=1 

for ev in trDat:
    print(ev)
    #for r in ev:
       # print(r)


#print listDat
#d = listData[0][0]
#print (x.strip(' ') for x in listDat[0][0])

l = listDat[0][0]
p = l.split()
print l.split()
print p[0]

## Gives length of rows in inverse array
print len(p)

lengthOfInverse = len(p)
