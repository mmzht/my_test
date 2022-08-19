import numpy as np
import matplotlib.pyplot as plt
##x = np.linspace(-2, 2, 1000)
##y1 = np.cos(40 * x)
##y2 = np.exp(-x**2)
##plt.plot(x,y1*y2)
##plt.show()

fig = plt.figure(figsize=(8, 2.5))
left, bottom, width, height = 0.1, 0.2, 0.8, 0.7
ax = fig.add_axes((left, bottom, width, height))
x = np.linspace(-2, 2, 1000)
y1 = np.cos(40 * x)
y2 = np.exp(-x**2)
ax.plot(x,y1*y2)
ax.plot(x,y2,'g')
ax.plot(x,-y2,'g')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
