import numpy as np
from matplotlib import collections
import matplotlib.pyplot as pylab

#make some oscillating data
panel = np.meshgrid(np.arange(1501), np.arange(284))[0]
panel = np.sin(panel)

#generate coordinate vectors.
panel[:,-1] = np.nan #lazy prevents polygon wrapping 
x = panel.ravel()
y = np.meshgrid(np.arange(1501), np.arange(284))[0].ravel() 

#find indexes of each zero crossing
zero_crossings = np.where(np.diff(np.signbit(x)))[0]+1 

#calculate scalars used to shift "traces" to plotting corrdinates
trace_centers = np.linspace(1,284, panel.shape[-2]).reshape(-1,1) 
gain = 0.5 #scale traces

#shift traces to plotting coordinates
x = ((panel*gain)+trace_centers).ravel()

#split coordinate vectors at each zero crossing
xpoly = np.split(x, zero_crossings)
ypoly = np.split(y, zero_crossings)

#we only want the polygons which outline positive values
if x[0] > 0:
    steps = range(0, len(xpoly),2)
else:
    steps = range(1, len(xpoly),2)

#turn vectors of polygon coordinates into lists of coordinate pairs
polygons = [zip(xpoly[i], ypoly[i]) for i in steps if len(xpoly[i]) > 2]

#this is so we can plot the lines as well
xlines = np.split(x, 284)
ylines = np.split(y, 284)
lines = [zip(xlines[a],ylines[a]) for a in range(len(xlines))]  

#and plot
fig = pylab.figure()
ax = fig.add_subplot(111)
col = collections.PolyCollection(polygons)
col.set_color('k')
ax.add_collection(col, autolim=True)
col1 = collections.LineCollection(lines)
col1.set_color('k')
ax.add_collection(col1, autolim=True)
ax.autoscale_view()
pylab.xlim([0,284])
pylab.ylim([0,1500])
ax.set_ylim(ax.get_ylim()[::-1])
pylab.tight_layout()
pylab.show()
