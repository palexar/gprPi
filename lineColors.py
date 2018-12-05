import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

#print("worked")

x = np.linspace(0,3*np.pi, 500)
y = np.sin(x)
z = np.cos(0.5 * (x[:-1] + x[1:]))
print(len(z))
xtest = np.linspace(0, 500, 500)
ytest = np.linspace(0, 500, 500)
ztest = np.linspace(0, 500, 500) 
cmap = ListedColormap(['r', 'g', 'b'])
norm = BoundaryNorm([-1, 0.3, 0.5, 1], cmap.N)


points = np.array([xtest,ytest]).T.reshape(-1,1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis = 1)

print("segments = "),
print(len(segments))

lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(ztest)
lc.set_linewidth(3)

fig1 = plt.figure()
plt.gca().add_collection(lc)
plt.xlim(x.min(), x.max())
plt.ylim(0, 500)

plt.show()
