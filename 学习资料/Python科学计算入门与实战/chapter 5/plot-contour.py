import numpy as np
import matplotlib.pyplot as plt
##plt.rcParams['font.sans-serif'] = ['SimHei']   
##plt.rcParams['axes.unicode_minus'] = False

delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X,Y = np.meshgrid(x,y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X-1)**2-(Y-1)**2)
Z = (Z1-Z2)

fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)

cs1 = ax1.contour(X,Y,Z,12,colors="k")
ax1.clabel(cs1,inline=1,fmt="%.2f")

cs2 = ax2.contour(X,Y,Z,levels=[0.2,0.4,0.6],
                  colors=["k","r","g"])
ax2.clabel(cs2,inline=0,fontsize=10)

levels = np.arange(-2.0, 1.601, 0.4)
cs3 = ax3.contourf(X,Y,Z,levels=levels,cmap="winter",alpha=0.5)

cs4 = ax4.contourf(X,Y,Z,levels=levels,cmap="hot",alpha=0.5)
cs44 = ax4.contour(X,Y,Z,levels=levels)

plt.show()
