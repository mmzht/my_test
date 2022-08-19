import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(111)
x = np.linspace(-5,5,50)
y = 1.4*x**3 + 3.3*x**2 + 2.8*x + 5*np.random.uniform(-3,4,50)
c = np.polyfit(x,y,3)
p = np.poly1d(c)
y_p  = np.polyval(p,x)
ax.scatter(x,y,color = "red",marker = ".",label = "data")
ax.plot(x,y_p,color = "green",label = "curve")
ax.legend()
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
plt.show()
