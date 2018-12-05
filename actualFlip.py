import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

def ge():
    t = []
    for i in range(1,26):
        t.append(i)
    return t

## is a list of data horizontally
t1 = np.arange(0.0, 5.0, 0.1)

t2 = []
counter = 0
for i in range(1,26):
    t2.append(i)

t3 = ge()
t4 = ge()

data = []
## turn data vertically then map horizontally
data.append(t2)
data.append(t3)
data.append(t4)

for i in data[0]:
    print data[0][i-1]

for i in data[0]:
    print data[1][i-1]
