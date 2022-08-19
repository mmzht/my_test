import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
def f(x):
    return np.sin(x)*x

fontsize = 12
fig = plt.figure(figsize=(10, 5))
rect1 = (0.1,0.1,0.8,0.8)
rect2 = (0.6,0.60,0.1,0.25)
ax1 = fig.add_axes(rect1)
ax2 = fig.add_axes(rect2)

x = np.linspace(-10,10,100)
ax1.plot(x,f(x),lw = 2)
ax1.set_xlabel("$x$",fontsize = fontsize)
ax1.set_ylabel("$f(x)$",fontsize = fontsize)

x0,x1 = 1.5,4.0
ax1.axvline(x0,ymin = 0.4,ymax = 0.6,color = "grey",ls = ":")
ax1.axvline(x1,ymin = 0.1,ymax = 0.3,color = "grey",ls = ":")
nx = np.linspace(x0,x1,100)
ax2.plot(nx,f(nx),lw = 2)
ax2.set_xlabel("$x$")
ax2.set_ylabel("$f(x)$")
ax2.xaxis.set_major_locator(mpl.ticker.MaxNLocator(4))
ax2.yaxis.set_major_locator(mpl.ticker.MaxNLocator(4))
plt.show()
