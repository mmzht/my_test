import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)
y= np.sin(x)*x
fig,ax = plt.subplots(figsize=(10, 5))
ax.plot(x,y,lw = 2)
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
ax.set_xticks([-10, -5, 5, 10])
ax.set_yticks([-10, 0, 10])
plt.show()
