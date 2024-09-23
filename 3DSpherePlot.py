import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.lines as Line2d
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm

# linespace(x, y, n) function returns a array with n values evenly spacing between [a, b]
theta = np.linspace(-np.pi, np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)

# meshgrid syncronise the index of theta and phi
theta, phi = np.meshgrid(theta, phi)
x = np.sin(theta) * np.cos(phi)
y = np.sin(theta) * np.sin(phi)
z = np.cos(theta)

# .figure() returns an figure instance
fig = plt.figure()

# 111/121/122 is a format code for subplots like 
# [111]/[121][122]
# projection is defaulted as '2d'
ax = fig.add_subplot(121, projection = '3d')
ay = fig.add_subplot(122, projection = '3d')

# cmap is the color format of the plot
ax.plot_surface(x, y, z, cmap = 'spring')
ay.plot_surface(y, z, x, cmap = 'Spectral')

plt.show()
