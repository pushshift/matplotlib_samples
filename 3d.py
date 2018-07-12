#!/usr/bin/env python3

import numpy as np
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MultipleLocator
import numpy as np
import imageio

def three_d():
    frames = []
    z = list(np.arange(.1, 2.0, 0.02)) + list(reversed(np.arange(.11, 2.0, 0.02)))
    for g in z:
        print(g)
        fig = plt.figure()
        ax = Axes3D(fig)
        X = np.arange(-4, 4, 0.15)
        Y = np.arange(-4, 4, 0.15)
        X, Y = np.meshgrid(X, Y)
        R = np.sqrt(X ** 2 + Y ** 2)
        Z = np.sin(R+g)*g
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)
        ax.set_zlim(-2, 2)
        fig.canvas.draw()       # draw the canvas, cache the renderer
        image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
        image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        plt.close(fig)
        plt.close('all')
        frames.append(image)
    return frames

frames = three_d()
imageio.mimsave('image.gif', frames, fps=30)

