import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-3,3,20)
y = 10*x                       #y=10x
x1 = np.linspace(-2,2,20)
y1 = 8*x1**2                  #y=8x2
x2 = np.linspace(-3,3,20)
y2 = x2**3                    #y=x3
plt.plot(x,y,"r-*",linewidth = 1.5)
plt.plot(x1,y1,"g--",linewidth = 0.9)
plt.plot(x2,y2,"k:",linewidth = 2.0)
plt.show()
