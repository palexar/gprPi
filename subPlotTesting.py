import numpy as np
import pylab as pl
from matplotlib import collections as mc

lines = [[(0, 1), (1, 1)], [(1, 1), (2, 1)], [(1, 2), (1, 3)], [(0,2), (1,2)]]
c = np.array([(1,0,0,1), (0, 1, 0, 1), (0, 0, 1, 1), (0, 1, 0, 1)]
)
lc = mc.LineCollection(lines, colors=c, linewidths=2)
fig, ax = pl.subplots()
ax.add_collection(lc)
ax.autoscale()
ax.margins(0.1)

pl.show()

print("Done")
