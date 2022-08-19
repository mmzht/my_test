import numpy as np
import matplotlib.pyplot as plt
##plt.rcParams['font.sans-serif'] = ['SimHei']   
##plt.rcParams['axes.unicode_minus'] = False

from mpl_toolkits.mplot3d import Axes3D

def title_and_labels(ax,title):
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    
fig,axes = plt.subplots(1,3,figsize=(12,3),
                        subplot_kw={'projection':'3d'})
x = y = np.linspace(-3, 3, 74)
X, Y = np.meshgrid(x,y)
R = np.sqrt(X**2+Y**2)
Z = np.sin(4*R)/R

p = axes[0].plot_surface(X,Y,Z,rstride=1,cstride=1,linewidth=0,
                         cmap="hot")
cb = fig.colorbar(p, ax=axes[0],shrink=0.6)
title_and_labels(axes[0],"surface")

axes[1].plot_wireframe(X,Y,Z,rstride=2,cstride=2,color="darkgrey")
title_and_labels(axes[1],"wireframe")

axes[2].contour(X,Y,Z, zdir='z',offset=0,cmap="hot")
axes[2].contour(X,Y,Z, zdir='y',offset=3,cmap="hot")
title_and_labels(axes[2],"contour")

plt.show()
