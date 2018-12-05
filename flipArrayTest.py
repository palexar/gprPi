

data = []
counter = 0
for i in range(1,26):
    data.append(i)

print data[0]

## prints out 1-25.
for counter in data:
    print data[counter-1]
    counter+=1
