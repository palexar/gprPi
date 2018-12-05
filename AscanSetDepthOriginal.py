import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from Tkinter import *

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.xlabel("Depth (meters)")
plt.ylabel("Strength of Wave Reflection")
plt.title("A Scan")
plt.plot(t1, f(t1), 'b')

plt.show()
