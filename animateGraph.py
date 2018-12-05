import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import datetime

x = 1
step = 0.1
prevX = x
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xs = []
ys = []


print("here is x")
print(x)


def animate(i, xs, ys):

    global x
    global prevX
    x = prevX + step
    prevX = x
    
    xs.append(x)
    ys.append(math.sin(x))

    xs = xs[-100:]
    ys = ys[-100:]

    ax.clear()
    ax.plot(xs,ys)

    #plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('A scan')
    plt.ylabel('Strength of Reflection')
    plt.xlabel('Distance Underground')
    print(x)
    print(math.sin(x))
    print(datetime.datetime.now())


ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(xs, ys), interval=20)
plt.show()
