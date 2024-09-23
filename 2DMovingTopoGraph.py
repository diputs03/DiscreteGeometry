import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.lines as Line2d
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm


n = 10
x = np.random.rand(n)
y = np.random.rand(n)
for c in range(n): 
    x[c] = np.random.rand() * 100
    y[c] = np.random.rand() * 100

fig = plt.figure()
ax = fig.add_subplot(111)

num_segments = 20

k1 = []
k2 = []

for c in range(num_segments):
    k1.append(int(np.random.rand() * 100) % n)
    k2.append(int(np.random.rand() * 100) % n)

def animate(t): 
    for i in range(n):
        x[i] += np.random.rand() - 0.5
        y[i] += np.random.rand() - 0.5
    plt.cla()
    plt.scatter(x, y)
    plt.plot([x[k1], x[k2]], [y[k1], y[k2]], marker = 'o', color = 'blue')

ani = FuncAnimation(plt.gcf(), animate, interval = 0.01)

plt.show()
